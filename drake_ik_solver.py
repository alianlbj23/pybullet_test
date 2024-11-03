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
    MinimumDistanceLowerBoundConstraint,
    SolverId,
    BodyIndex,
    FrameIndex,
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
        
        # 檢查所有可用的 body 名稱
        print("\n可用的 body 名稱：")
        for body_index in range(self.plant.num_bodies()):
            body = self.plant.get_body(BodyIndex(body_index))
            print(f"Body {body_index}: {body.name()}")
        
        # 檢查所有可用的 frame 名稱
        print("\n可用的 frame 名稱：")
        for frame_index in range(self.plant.num_frames()):
            frame = self.plant.get_frame(FrameIndex(frame_index))
            print(f"Frame {frame_index}: {frame.name()}")
        
        # 獲取末端執行器（使用最後一個 link 或正確的名稱）
        try:
            self.end_effector = self.plant.GetBodyByName("robot_ver7_grap1_2_v1_1")
        except RuntimeError:
            print("找不到指定的末端執行器，嘗試列出所有 bodies...")
            # 如果找不到，使用最後一個非 world body
            last_body = None
            for body_index in range(self.plant.num_bodies()):
                body = self.plant.get_body(BodyIndex(body_index))
                if body.name() != "world":
                    last_body = body
            self.end_effector = last_body
        
        print(f"\n使用的末端執行器: {self.end_effector.name()}")
        
        # 獲取末端執行器的當前位置
        current_pose = self.plant.EvalBodyPoseInWorld(
            self.plant_context, self.end_effector)
        current_position = current_pose.translation()
        print(f"末端執行器當前位置: {current_position}")
        
        # 重新創建系統以���用位移
        self._recreate_system()
        
        # 直接將基座固定在原點
        X_offset = RigidTransform()  # 不設置偏移量，使用默認的單位變換
        print(f"設定偏移量: {X_offset.translation()}")
        
        # 將基座焊接到世界坐標系原點
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
        解算運動學
        
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
            
            # 印出更多診斷信息
            print("\n診斷信息：")
            print(f"末端執行器名稱: {self.end_effector.name()}")
            current_pose = self.plant.EvalBodyPoseInWorld(
                self.plant_context, self.end_effector)
            current_position = current_pose.translation()
            print(f"當前位置: {current_position}")
            print(f"目標位: {target_position}")
            print(f"位置差異: {np.linalg.norm(current_position - target_position)}")
            
            # 添加關節限位約束
            for joint_index in range(self.plant.num_joints()):
                joint = self.plant.get_joint(JointIndex(joint_index))
                if joint.type_name() == "RevoluteJoint":
                    # 獲取關節的運動學限制
                    lower_limit = joint.position_lower_limit()
                    upper_limit = joint.position_upper_limit()
                    
                    # 打印關節信息
                    print(f"關節 {joint.name()}:")
                    print(f"  位置限制: [{lower_limit}, {upper_limit}]")
                    
                    # 添加位置限制（增加一些容差）
                    if lower_limit > -np.inf and upper_limit < np.inf:
                        tolerance = 0.1  # 增加一些容差
                        ik.AddPositionConstraint(
                            joint,
                            lower_limit - tolerance,
                            upper_limit + tolerance
                        )
            
            # 設置目標位置約束（使用較大的容差）
            pos_tolerance = 0.05  # 5cm的容差
            ik.AddPositionConstraint(
                frameA=self.plant.world_frame(),
                frameB=self.end_effector.body_frame(),  # 使用末端執行器的 body frame
                p_BQ=np.zeros(3),
                p_AQ_lower=[x - pos_tolerance for x in target_position],
                p_AQ_upper=[x + pos_tolerance for x in target_position]
            )
            
            # 設置更好的初始猜測值 - 使用多個隨機初���值
            prog = ik.prog()
            num_attempts = 10  # 嘗試多個初始猜測值
            
            for attempt in range(num_attempts):
                if attempt == 0:
                    # 第一次使用當前位置
                    q_guess = self.plant.GetPositions(self.plant_context)
                else:
                    # 後續使用隨機值，但在合理範圍內
                    q_guess = np.zeros(self.plant.num_positions())
                    for joint_index in range(self.plant.num_joints()):
                        joint = self.plant.get_joint(JointIndex(joint_index))
                        if joint.type_name() == "RevoluteJoint":
                            lower = joint.position_lower_limit()
                            upper = joint.position_upper_limit()
                            if lower > -np.inf and upper < np.inf:
                                q_guess[joint_index] = np.random.uniform(lower, upper)
                
                print(f"嘗試初始猜測值 {attempt + 1}: {q_guess}")
                prog.SetInitialGuess(ik.q(), q_guess)
                
                # 求解 IK
                result = Solve(prog)
                
                if result.is_success():
                    print(f"在第 {attempt + 1} 次嘗試中成功求解")
                    break
                else:
                    print(f"第 {attempt + 1} 次嘗試失敗")
                    if attempt < num_attempts - 1:
                        continue
                    else:
                        print(f"所有嘗試都失敗了")
                        return False, None
            
            # 獲取關節角度解
            q = result.GetSolution(ik.q())
            
            # 應用解算結果並驗證
            self.plant.SetPositions(self.plant_context, self.model_instance, q)
            end_pose = self.plant.EvalBodyPoseInWorld(self.plant_context, self.end_effector)
            actual_position = end_pose.translation()
            
            print(f"目標位置: {target_position}")
            print(f"實際位置: {actual_position}")
            print(f"最終關節角度解: {q}")
            
            # 更新視覺化
            self.simulator.AdvanceTo(0.0)
            visualizer_context = self.diagram.GetSubsystemContext(
                self.visualizer, self.context)
            self.visualizer.ForcedPublish(visualizer_context)
            
            return True, q
            
        except Exception as e:
            print(f"IK 求解時發生錯誤: {str(e)}")
            return False, None

    def set_joint_positions(self, angles=None):
        """
        設置關節角度，但保持 base_link 不變
        """
        try:
            # 獲取當前關節位置
            current_positions = self.plant.GetPositions(self.plant_context)
            new_positions = current_positions.copy()
            
            print("\n設置關節角度：")
            for joint_index in range(self.plant.num_joints()):
                joint = self.plant.get_joint(JointIndex(joint_index))
                if joint.type_name() == "RevoluteJoint":
                    joint_name = joint.name()
                    print(f"檢查關節: {joint_name}")
                    
                    # 跳過 base_link 相關的關節
                    if "base" in joint_name.lower():
                        print(f"  跳過 base 關節: {joint_name}")
                        continue
                    
                    # 設置其他關節為 90 度
                    joint_position_index = joint.position_start()
                    new_positions[joint_position_index] = np.pi/2
                    print(f"  設置關節 {joint_name} 為 90 度")
            
            # 應用新的關節角度
            self.plant.SetPositions(self.plant_context, self.model_instance, new_positions)
            
            # 更新��覺化
            self.simulator.AdvanceTo(0.0)
            visualizer_context = self.diagram.GetSubsystemContext(
                self.visualizer, self.context)
            self.visualizer.ForcedPublish(visualizer_context)
            
            # 打印設置後的位置
            current_pose = self.plant.EvalBodyPoseInWorld(
                self.plant_context, self.end_effector)
            print(f"\n設置後末端執行器位置: {current_pose.translation()}")
            print(f"最終關節角度: {new_positions}")
            
            return True
            
        except Exception as e:
            print(f"設置關節角度時發生錯誤: {str(e)}")
            return False

def main():
    # 創建機器人控制器實例
    robot = RobotArmIK()
    
    # 設置除了 base_link 外的所有關節為 90 度
    print("設置關節角度...")
    # success = robot.set_joint_positions()
    
    # if success:
    #     print("關節角度設置成功！")
    # else:
    #     print("關節角度設置失敗。")
    
    # 保持程序運行
    input("按Enter鍵結束...")

if __name__ == "__main__":
    main()
