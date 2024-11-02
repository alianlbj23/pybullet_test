from pydrake.all import (
    Parser,
    MultibodyPlant,
    AddMultibodyPlantSceneGraph,
    DiagramBuilder,
    Simulator,
    MeshcatVisualizer,
    StartMeshcat,
    RigidTransform,
    RotationMatrix,
    InverseKinematics,
    Frame,
    Solve,
    JointIndex,
    Box,
    Rgba,
)
import numpy as np
import webbrowser

class RobotArmIK:
    def __init__(self):
        # 啟動 Meshcat 視覺化服務器
        self.meshcat = StartMeshcat()
        
        # 自動打開瀏覽器
        webbrowser.open(self.meshcat.web_url())
        
        # 清除之前的視覺化
        self.meshcat.Delete()
        
        print(f"Meshcat URL: {self.meshcat.web_url()}")
        
        # 創建系統圖
        self.builder = DiagramBuilder()
        
        # 創建多體系統和場景圖
        self.plant, self.scene_graph = AddMultibodyPlantSceneGraph(
            self.builder, time_step=0.0)
        
        # 禁用重力
        self.plant.mutable_gravity_field().set_gravity_vector([0, 0, 0])
        
        # 創建解析器並載入URDF
        self.parser = Parser(self.plant)
        self.model_instance = self.parser.AddModels("excurate_arm/target.urdf")[0]
        
        # 在 Finalize 之前添加固定約束
        world_frame = self.plant.world_frame()
        base_frame = self.plant.GetFrameByName("base_link")
        
        # 使用 WeldFrames 而不是 AddWeld
        self.plant.WeldFrames(
            world_frame,  # 父框架（世界坐標系）
            base_frame,   # 子框架（機器人基座）
            RigidTransform()  # 身份變換（保持在原點）
        )
        
        self.plant.Finalize()
        
        # 添加視覺化器並獲取其實例
        self.visualizer = MeshcatVisualizer.AddToBuilder(
            self.builder, self.scene_graph, self.meshcat)
        
        # 構建系統圖
        self.diagram = self.builder.Build()
        
        # 創建模擬器
        self.simulator = Simulator(self.diagram)
        self.context = self.simulator.get_mutable_context()
        
        # 保存重要的引用
        self.plant_context = self.diagram.GetMutableSubsystemContext(
            self.plant, self.context)
        self.base_body = self.plant.GetBodyByName("base_link")
        self.end_effector = self.plant.GetBodyByName("robot_ver7_grap1_2_v1_1")
        
        # 初始化模擬器
        self.simulator.Initialize()
        
        try:
            # 設置所有關節的初始位置為0
            num_positions = self.plant.num_positions()
            initial_positions = np.zeros(num_positions)
            self.plant.SetPositions(self.plant_context, self.model_instance, initial_positions)
            
            # 更新視覺化
            self.simulator.AdvanceTo(0.0)
            visualizer_context = self.diagram.GetSubsystemContext(
                self.visualizer, self.context)
            self.visualizer.ForcedPublish(visualizer_context)
            
        except Exception as e:
            print(f"初始化時發生錯誤: {str(e)}")
        
    def solve_ik(self, target_position, target_rotation=None):
        """
        解算逆運動學
        
        Args:
            target_position: 目標位置 [x, y, z]
            target_rotation: 目標旋轉（可選）
            
        Returns:
            success: 是否成功求解
            q: 關節角度解
        """
        try:
            # 添加目標位置的可視化方塊
            self.meshcat.SetObject(
                "/target_marker",           # 可視化對象的名稱
                Box(0.1, 0.1, 0.1),        # 方塊大小 (10cm x 10cm x 10cm)
                Rgba(1.0, 0.0, 0.0, 0.8)   # 紅色，半透明
            )
            # 設置方塊位置
            self.meshcat.SetTransform(
                "/target_marker",
                RigidTransform(p=target_position)
            )
            
            # 創建 IK 求解器
            ik = InverseKinematics(self.plant, self.plant_context)
            
            # 獲取末端執行器框架
            end_frame = self.plant.GetFrameByName("robot_ver7_grap1_2_v1_1")
            world_frame = self.plant.world_frame()
            
            # 打印當前位置
            current_pose = self.plant.EvalBodyPoseInWorld(
                self.plant_context, self.end_effector)
            print(f"當前位置: {current_pose.translation()}")
            
            # 添加關節限位約束
            for joint_index in range(self.plant.num_joints()):
                joint = self.plant.get_joint(JointIndex(joint_index))
                if joint.type_name() == "RevoluteJoint":
                    # 設置關節角度限制（根據實際情況調整）
                    ik.AddPositionConstraint(
                        joint,
                        -np.pi,  # 下限
                        np.pi    # 上限
                    )
            
            # 設置目標位置約束（使用較小的容差）
            pos_tolerance = 0.01  # 1cm的容差
            ik.AddPositionConstraint(
                frameA=world_frame,
                frameB=end_frame,
                p_BQ=np.zeros(3),
                p_AQ_lower=[x - pos_tolerance for x in target_position],
                p_AQ_upper=[x + pos_tolerance for x in target_position]
            )
            
            # 如果有指定旋轉，添加旋轉約束
            if target_rotation is not None:
                ik.AddOrientationConstraint(
                    frameA=world_frame,
                    frameB=end_frame,
                    target_rotation=target_rotation,
                    angle_bound=0.1
                )
            
            prog = ik.prog()
            
            # 設置初始猜測值
            q0 = np.zeros(self.plant.num_positions())
            prog.SetInitialGuess(ik.q(), q0)
            
            # 求解 IK
            result = Solve(prog)
            
            if not result.is_success():
                print(f"IK 求解失敗，狀態: {result.get_solution_result()}")
                return False, None
            
            # 獲取關節角度解
            q = result.GetSolution(ik.q())
            
            # 應用解算結果
            self.plant.SetPositions(self.plant_context, self.model_instance, q)
            
            # 更新視覺化
            self.simulator.AdvanceTo(0.0)
            visualizer_context = self.diagram.GetSubsystemContext(
                self.visualizer, self.context)
            self.visualizer.ForcedPublish(visualizer_context)
            
            # 驗證結果
            end_pose = self.plant.EvalBodyPoseInWorld(
                self.plant_context, self.end_effector)
            actual_position = end_pose.translation()
            
            print(f"目標位置: {target_position}")
            print(f"實際位置: {actual_position}")
            print(f"關節角度解: {q}")
            
            return True, q
            
        except Exception as e:
            print(f"IK 求解時發生錯誤: {str(e)}")
            return False, None

def main():
    # 創建機器人控制器實例
    robot = RobotArmIK()
    
    # 測試 IK 求解 - 使用更小的目標位置值
    target_pos = [0.0, 0.0, 0.0]  # 設置一個更近的目標位置
    success, joint_angles = robot.solve_ik(target_pos)
    
    if success:
        print("IK 求解成功！")
    else:
        print("IK 求解失敗。")
    
    # 保持程序運行
    input("按Enter鍵結束...")

if __name__ == "__main__":
    main()
