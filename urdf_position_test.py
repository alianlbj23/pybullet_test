import pybullet as p
import time
import os

p.connect(p.GUI)
urdf_path = os.path.abspath("./excurate_arm/target.urdf")
robot_id = p.loadURDF(urdf_path, basePosition=[0, 0, 0], useFixedBase=True)

# 獲取 base_link 的位置
base_position, base_orientation = p.getBasePositionAndOrientation(robot_id)
print(f"Base Position: {base_position}")
print(f"Base Orientation: {base_orientation}")

# 檢查其他連接點位置
for i in range(p.getNumJoints(robot_id)):
    link_state = p.getLinkState(robot_id, i)
    print(f"Link {i} Position: {link_state[0]}")
    print(f"Link {i} Orientation: {link_state[1]}")
    
time.sleep(5)  # 暫停以便觀察
p.disconnect()
