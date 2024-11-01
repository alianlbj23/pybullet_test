import math
import numpy as np
from roboticstoolbox.robot.Robot import Robot
from roboticstoolbox.backends.PyPlot import PyPlot
from spatialmath.base import transl
from spatialmath import SE3

def radian_to_degree(values):
    return [math.degrees(value) if value != -1 else -1 for value in values]

class ExcurateArm(Robot):
    def __init__(self):
        # 讀取 URDF
        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "target.urdf",
            "./excurate_arm"
        )
        print(f"Number of links: {len(links)}")
        print("Links:", [link.name for link in links])
        
        super().__init__(
            links,
            name=name,
            manufacturer="Excurate",
            gripper_links=links[-1],
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
        )
        
        # 初始化機器人姿態為90度
        self.q = np.full(5, np.pi/2)  # 5個關節都設為90度
        print(f"初始關節角度（度）: {np.degrees(self.q)}")
        
        # 初始化 PyPlot 視覺化環境
        print("正在初始化視覺化環境...")
        self.env = PyPlot()
        self.env.launch()
        self.env.add(self)
        self.env.step()
        print("視覺化環境初始化完成")

    def solve_ik(self, x, y, z):
        target_position = transl(x, y, z)
        return self.ikine_LM(target_position, end=self.links[-1], q0=self.q, mask=[1, 1, 1, 0, 0, 0])

    def test_ik(self, x, y, z):
        print(f"\n測試 IK 求解，目標位置: ({x}, {y}, {z})")
        solution = self.solve_ik(x, y, z)
        
        if solution.success:
            print("IK 求解成功!")
            print(f"計算出的關節角度（度）: {np.degrees(solution.q)}")
            
            # 緩慢移動到目標位置
            steps = 50
            q_start = self.q.copy()
            q_end = solution.q
            
            for i in range(steps):
                alpha = (i + 1) / steps
                self.q = (1 - alpha) * q_start + alpha * q_end
                self.env.step()
        else:
            print(f"IK 求解失敗: 無法到達位置 ({x}, {y}, {z})")

def main():
    # 創建機器人實例
    robot = ExcurateArm()
    
    # 等待使用者確認初始位置
    input("\n按 Enter 開始 IK 測試...")
    
    # 測試一些位置
    test_positions = [
        (0.3, 0.0, 0.3),
        (0.3, 0.2, 0.3),
        (0.3, -0.2, 0.3)
    ]
    
    for x, y, z in test_positions:
        input(f"\n按 Enter 移動到位置 ({x}, {y}, {z})...")
        robot.test_ik(x, y, z)
    
    input("\n按 Enter 結束程式...")

if __name__ == "__main__":
    main()
