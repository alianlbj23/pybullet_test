from pydrake.all import (
    Parser,
    MultibodyPlant,
    AddMultibodyPlantSceneGraph,
    DiagramBuilder,
    Simulator,
    MeshcatVisualizer,
    StartMeshcat,
    RigidTransform,
    RotationMatrix
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
        
        # 創建解析器並載入URDF
        self.parser = Parser(self.plant)
        self.model_instance = self.parser.AddModels("excurate_arm/target.urdf")[0]
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
        
        # 初始化模擬器
        self.simulator.Initialize()
        
        try:
            # 獲取當前位置
            current_pose = self.plant.GetFreeBodyPose(self.plant_context, self.base_body)
            current_position = current_pose.translation()
            print(f"移動前機器人位置 (米): {current_position}")
            
            # 創建新的變換 - 移動到世界座標原點
            new_transform = RigidTransform(
                R=RotationMatrix(),
                p=np.array([0.0, 0.0, 0.0])  # 直接設置到世界座標原點
            )
            
            # 應用新位置
            self.plant.SetFreeBodyPose(self.plant_context, self.base_body, new_transform)
            
            # 更新視覺化
            self.simulator.AdvanceTo(0.0)
            visualizer_context = self.diagram.GetSubsystemContext(
                self.visualizer, self.context)
            self.visualizer.ForcedPublish(visualizer_context)
            
            # 獲取更新後的位置
            updated_pose = self.plant.GetFreeBodyPose(self.plant_context, self.base_body)
            print(f"移動後機器人位置 (米): {updated_pose.translation()}")
            
        except Exception as e:
            print(f"計算時發生錯誤: {str(e)}")

def main():
    # 創建機器人控制器實例
    robot = RobotArmIK()
    
    # 保持程序運行
    input("按Enter鍵結束...")

if __name__ == "__main__":
    main()
