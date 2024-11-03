from ament_index_python.packages import get_package_share_directory
import pydrake.all as drake
import numpy as np
import os

class DrakeIKSolver:
    def __init__(self, urdf_name="pros_car.urdf"):
        # 設置 URDF 路徑
        package_path = get_package_share_directory('pros_car_description')
        urdf_path = os.path.join(package_path, 'urdf', urdf_name)
        
        # 建立 Drake 的多體系統
        self.builder = drake.systems.DiagramBuilder()
        self.plant = drake.multibody.plant.MultibodyPlant(0.0)
        drake.multibody.parsing.Parser(self.plant).AddModelFromFile(urdf_path)
        self.plant.Finalize()
        
        # 獲取重要的 frame 參考
        self.world_frame = self.plant.world_frame()
        self.ee_frame = self.plant.GetFrameByName("end_effector")  # 請根據你的 URDF 修改末端執行器的名稱
        
    def solve_ik(self, target_pos, target_rot=None):
        """
        解算逆運動學
        :param target_pos: [x, y, z] 目標位置
        :param target_rot: [roll, pitch, yaw] 目標旋轉（可選）
        :return: 關節���度列表
        """
        context = self.plant.CreateDefaultContext()
        
        # 建立 IK 問題
        ik = drake.multibody.inverse_kinematics.InverseKinematics(self.plant)
        
        # 添加位置約束
        p_target = target_pos
        ik.AddPositionConstraint(
            self.ee_frame,
            np.zeros(3),  # frame 上的點
            self.world_frame,
            p_target,
            p_target
        )
        
        # 如果有指定旋轉，添加旋轉約束
        if target_rot is not None:
            R_target = drake.math.RollPitchYaw(target_rot).ToRotationMatrix()
            ik.AddOrientationConstraint(
                self.ee_frame,
                self.world_frame,
                R_target,
                0.0  # 容許誤差
            )
        
        # 解算 IK
        result = drake.solvers.Solve(ik.prog())
        
        if not result.is_success():
            return None
            
        # 獲取結果
        q_sol = result.GetSolution(ik.q())
        return q_sol.tolist()

    def get_joint_limits(self):
        """
        獲取關節限制
        :return: (lower_limits, upper_limits)
        """
        num_positions = self.plant.num_positions()
        lower_limits = np.zeros(num_positions)
        upper_limits = np.zeros(num_positions)
        
        for i in range(num_positions):
            lower_limits[i] = self.plant.GetPositionLowerLimit(i)
            upper_limits[i] = self.plant.GetPositionUpperLimit(i)
            
        return lower_limits.tolist(), upper_limits.tolist()
