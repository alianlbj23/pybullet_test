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
        # 初始化基本系統
        self._initialize_system()
        
        # 先進行部分初始化以獲取位置
        self.plant.Finalize()
        self.diagram = self.builder.Build()
        self.simulator = Simulator(self.diagram)
        self.context = self.simulator.get_mutable_context()
        self.plant_context = self.diagram.GetMutableSubsystemContext(
            self.plant, self.context)
        
        # 獲取末端執行器
        self.end_effector = self.plant.GetBodyByName("base_link2_v2_1")
        
        # 獲取末端執行器的當前位置
        current_pose = self.plant.EvalBodyPoseInWorld(
            self.plant_context, self.end_effector)
        current_position = current_pose.translation()
        print(f"末端執行器當前位置: {current_position}")
        
        # 重新創建系統以應用位移
        self._recreate_system()
        
        # 設置偏移量，但 Z 軸保持為 0
        offset = [-current_position[0],  # X 軸取負
                 -current_position[1],   # Y 軸取負
                 0]                      # Z 軸設為 0
        
        X_offset = RigidTransform(p=offset)
        print(f"設定偏移量: {X_offset.translation()}")
        
        # 現在可以安全地進行焊接
        self.plant.WeldFrames(
            self.world_frame,
            self.plant.GetFrameByName("base_link"),
            X_offset
        )
        
        # 完成最終初始化
        self._complete_initialization()

    def _initialize_system(self):
        """初始化基本系統和組件"""
        # 啟動 Meshcat 視覺化服務器
        self.meshcat = StartMeshcat()
        webbrowser.open(self.meshcat.web_url())
        self.meshcat.Delete()
        print(f"Meshcat URL: {self.meshcat.web_url()}")
        
        # 添加目標方塊
        self.meshcat.SetObject(
            "/target_marker",
            Box(0.1, 0.1, 0.1),        # 方塊大小 (10cm x 10cm x 10cm)
            Rgba(1.0, 0.0, 0.0, 0.8)   # 紅色，半透明
        )
        
        # 設置方塊初始位置
        target_position = [0.0, 0.0, 0.0]  # 可以根據需要調整
        self.meshcat.SetTransform(
            "/target_marker",
            RigidTransform(p=target_position)
        )
        
        # 打印方塊位置
        print(f"目標方塊位置: {target_position}")
        
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
        
        # 獲取必要的 frame 和 body
        self.world_frame = self.plant.world_frame()
        self.base_body = self.plant.GetBodyByName("base_link")

    def _recreate_system(self):
        """重新創建系統"""
        self.builder = DiagramBuilder()
        self.plant, self.scene_graph = AddMultibodyPlantSceneGraph(
            self.builder, time_step=0.0)
        self.plant.mutable_gravity_field().set_gravity_vector([0, 0, 0])
        self.parser = Parser(self.plant)
        self.model_instance = self.parser.AddModels("excurate_arm/target.urdf")[0]
        self.world_frame = self.plant.world_frame()
        self.base_body = self.plant.GetBodyByName("base_link")

    def _complete_initialization(self):
        """完成剩餘的初始化步驟"""
        # 完成系統設置
        self.plant.Finalize()
        
        # 添加視覺化器
        self.visualizer = MeshcatVisualizer.AddToBuilder(
            self.builder, self.scene_graph, self.meshcat)
        
        # 構建系統圖
        self.diagram = self.builder.Build()
        
        # 創建模擬器
        self.simulator = Simulator(self.diagram)
        self.context = self.simulator.get_mutable_context()
        self.plant_context = self.diagram.GetMutableSubsystemContext(
            self.plant, self.context)
        self.end_effector = self.plant.GetBodyByName("robot_ver7_grap1_2_v1_1")
        
        # 初始化模擬器
        self.simulator.Initialize()
        
        # 更新視覺化
        self.simulator.AdvanceTo(0.0)
        visualizer_context = self.diagram.GetSubsystemContext(
            self.visualizer, self.context)
        self.visualizer.ForcedPublish(visualizer_context)

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
            
            # 打印方塊位置
            print(f"目標方塊位置: {target_position}")
            
            # 創建 IK 求解器
            ik = InverseKinematics(self.plant, self.plant_context)
            
            # 獲取末端執行器框架
            end_frame = self.plant.GetFrameByName("robot_ver7_grap1_2_v1_1")
            world_frame = self.plant.world_frame()
            
            # 印當前位置
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
            print(f"關節��度解: {q}")
            
            return True, q
            
        except Exception as e:
            print(f"IK 求解時發生錯誤: {str(e)}")
            return False, None

def main():
    # 創建機器人控制器實例
    robot = RobotArmIK()
    
    # 測試 IK 求解 - 使用更小的目標位置值
    target_pos = [0.1, 0.1, 0.1]  # 設置一個更近的目標位置
    success, joint_angles = robot.solve_ik(target_pos)
    
    if success:
        print("IK 求解成功！")
    else:
        print("IK 求解失敗。")
    
    # 保持程序運行
    input("按Enter鍵結束...")

if __name__ == "__main__":
    main()
