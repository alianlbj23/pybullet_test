import pybullet as p
import pybullet_data
import numpy as np
import time
import os

class RobotArmController:
    def __init__(self):
        # 初始化 PyBullet
        self.physics_client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        
        # 設置環境
        self.setup_environment()
        
        # 載入機器人
        self.robot_id = self.load_robot()
        
        # 設置模擬參數
        self.use_realtime = False  # 不使用實時模擬

    def setup_environment(self):
        """設置模擬環境"""
        p.setGravity(0, 0, 0)
        p.loadURDF("plane.urdf")
        p.resetDebugVisualizerCamera(
            cameraDistance=1.0,
            cameraYaw=45,
            cameraPitch=-20,
            cameraTargetPosition=[0, 0, 0]
        )
        p.addUserDebugLine([0, 0, 0], [0.2, 0, 0], [1, 0, 0])
        p.addUserDebugLine([0, 0, 0], [0, 0.2, 0], [0, 1, 0])
        p.addUserDebugLine([0, 0, 0], [0, 0, 0.2], [0, 0, 1])

    def load_robot(self):
        """載入機器人模型"""
        urdf_path = os.path.abspath("./excurate_arm/target.urdf")
        print(f"載入 URDF: {urdf_path}")
        robot_id = p.loadURDF(
            urdf_path,
            basePosition=[0, 0, 0],
            baseOrientation=p.getQuaternionFromEuler([0, 0, 0]),
            useFixedBase=True
        )
        self.print_joint_info(robot_id)
        return robot_id

    def print_joint_info(self, robot_id):
        """打印關節信息"""
        num_joints = p.getNumJoints(robot_id)
        for i in range(num_joints):
            joint_info = p.getJointInfo(robot_id, i)
            print(f"關節 {i}: {joint_info[1].decode('utf-8')}, 類型: {joint_info[2]}")
            if joint_info[8] != joint_info[9]:
                print(f"  限制: [{np.degrees(joint_info[8]):.1f}, {np.degrees(joint_info[9]):.1f}] 度")

    def get_movable_joint_indices(self):
        """獲取可移動關節的索引"""
        return [i for i in range(p.getNumJoints(self.robot_id)) if p.getJointInfo(self.robot_id, i)[2] != p.JOINT_FIXED]

    def solve_ik(self, target_position, target_orientation=None, damping=0.01):
        """求解逆運動學"""
        end_effector_name = "robot_ver7_link_4_v1_1"  # 替換為 URDF 中的末端執行器名稱
        end_effector_index = self.get_link_index_by_name(end_effector_name)
        target_orientation = target_orientation or p.getQuaternionFromEuler([0, 0, 0])

        # 求解 IK，並設置阻尼
        joint_damping = [damping] * p.getNumJoints(self.robot_id)
        joint_poses = p.calculateInverseKinematics(
            self.robot_id,
            end_effector_index,
            target_position,
            target_orientation,
            jointDamping=joint_damping,
            maxNumIterations=200,  # Increase iterations
            residualThreshold=1e-5
        )
        
        # Debugging: Print joint poses
        print(f"目標位置: {target_position}")
        print(f"計算的關節角度（度）: {np.degrees(joint_poses)}")
        
        # 僅返回可動關節的角度
        movable_joints = self.get_movable_joint_indices()
        print("movable_joints:",movable_joints)
        movable_joint_poses = [joint_poses[i] for i in movable_joints if i < len(joint_poses)]
        # if len(movable_joint_poses) != len(movable_joints):
        #     raise ValueError("逆運動學計算的關節角度數量不匹配可動關節數量")
        
        # Verify end effector position
        p.setJointMotorControlArray(self.robot_id, movable_joints, p.POSITION_CONTROL, targetPositions=movable_joint_poses)
        p.stepSimulation()
        end_state = p.getLinkState(self.robot_id, end_effector_index)
        print(f"計算的末端執行器位置: {end_state[0]}")
        
        return movable_joint_poses

    def get_link_index_by_name(self, link_name):
        """根據鏈結名稱獲取鏈結索引"""
        num_joints = p.getNumJoints(self.robot_id)
        for i in range(num_joints):
            if p.getJointInfo(self.robot_id, i)[12].decode("utf-8") == link_name:
                return i
        raise ValueError(f"Link with name '{link_name}' not found.")

    def move_to_target(self, target_position, steps=1000):
        """移動到目標位置"""
        # 添加視覺標記（紅色方塊）
        visual_shape_id = p.createVisualShape(
            shapeType=p.GEOM_BOX,
            halfExtents=[0.02, 0.02, 0.02],  # 方塊大小
            rgbaColor=[1, 0, 0, 0.7]  # 紅色，稍微透明
        )
        target_marker = p.createMultiBody(
            baseMass=0,  # 質量為0表示靜態物體
            baseVisualShapeIndex=visual_shape_id,
            basePosition=target_position
        )

        # 求解 IK
        joint_poses = self.solve_ik(target_position)
        
        if joint_poses is not None:
            print("\nIK 求解成功!")
            movable_joints = self.get_movable_joint_indices()
            print("movable_joints:",movable_joints)
            
            # Debugging: Print lengths
            print(f"可動關節數量: {len(movable_joints)}")
            print(f"IK 求解關節角度數量: {len(joint_poses)}")
            
            # 逐步移動到目標位置
            for step in range(steps + 1):
                t = step / steps
                for idx, joint_index in enumerate(movable_joints):
                    if idx < len(joint_poses):  # Ensure index is within bounds
                        angle = (1 - t) * p.getJointState(self.robot_id, joint_index)[0] + t * joint_poses[idx]
                        p.setJointMotorControl2(
                            self.robot_id,
                            joint_index,
                            p.POSITION_CONTROL,
                            targetPosition=angle
                        )
                
                # 更新模擬
                p.stepSimulation()
                time.sleep(1./240.)  # 控制模擬速度
                
                # 打印進度
                if step % 10 == 0:
                    print(f"\n步驟 {step}/{steps}")
                    end_state = p.getLinkState(self.robot_id, movable_joints[-1])
                    print(f"當前位置: {end_state[0]}")
            
            return True
        return False

    def move_to_origin(self):
        """強制移動機器人到原點"""
        print("\n正在移動機器人到原點...")
        
        # 獲取基座位置
        base_pos, base_orn = p.getBasePositionAndOrientation(self.robot_id)
        print(f"當前基座位置: {base_pos}")
        
        # 設置新的基座位置
        new_pos = [0, 0, 0]  # 原點
        p.resetBasePositionAndOrientation(
            self.robot_id,
            new_pos,
            p.getQuaternionFromEuler([0, 0, 0])  # 保持原始方向
        )
        
        # 驗證新位置
        new_base_pos, _ = p.getBasePositionAndOrientation(self.robot_id)
        print(f"新基座位置: {new_base_pos}")
        
        # 重置所有關節到零位
        for i in range(p.getNumJoints(self.robot_id)):
            p.resetJointState(self.robot_id, i, 0)

    def cleanup(self):
        """清理資源"""
        p.disconnect()

def main():
    controller = RobotArmController()
    controller.move_to_origin()
    target_position = [-0.2, -0.3, 0.2]
    success = controller.move_to_target(target_position)
    if success:
        print("\n移動到指定位置成功!")
    else:
        print("\n移動到指定位置失敗!")
    controller.cleanup()

if __name__ == "__main__":
    main()
