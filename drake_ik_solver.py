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
            self.builder, time_step=0.001)
        
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
        
        try:
            # 初始化模擬器
            self.simulator.Initialize()
            
            # 獲取 plant context
            plant_context = self.diagram.GetMutableSubsystemContext(
                self.plant, self.context)
            
            # 獲取所有位置的數量
            num_positions = self.plant.num_positions()
            
            # 創建初始位置向量
            # 前7個值通常是基座的位置和方向（位置xyz + 四元數wxyz）
            desired_positions = np.zeros(num_positions)
            if num_positions >= 7:
                # 設置一個有效的四元數 (w=1, x=0, y=0, z=0 表示無旋轉)
                desired_positions[3] = 1.0  # w component of quaternion
            
            # 設置位置
            self.plant.SetPositions(plant_context, desired_positions)
            
            # 更新視覺化
            self.simulator.AdvanceTo(0.0)
            
            # 確認新位置
            current_positions = self.plant.GetPositions(plant_context)
            print(f"機器人位置: {current_positions}")
            
        except Exception as e:
            print(f"警告：{str(e)}")

if __name__ == "__main__":
    # 創建機器人控制器實例
    robot = RobotArmIK()
    
    # 保持程序運行
    input("按Enter鍵結束...")
