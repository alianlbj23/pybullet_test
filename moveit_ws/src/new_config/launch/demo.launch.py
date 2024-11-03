from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch import LaunchDescription
from launch.actions import LogInfo
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # 創建配置
    moveit_config = MoveItConfigsBuilder("angle_excurate_arm_ver2", package_name="new_config").to_moveit_configs()
    
    # 獲取 SRDF 文件路徑
    srdf_file = os.path.join(
        get_package_share_directory("new_config"),
        "config",
        "angle_excurate_arm_ver2.srdf"
    )
    
    # 檢查文件是否存在
    srdf_exists = os.path.isfile(srdf_file)
    
    return LaunchDescription([
        LogInfo(msg=['SRDF file path: ', srdf_file]),
        LogInfo(msg=['SRDF file exists: ', str(srdf_exists)]),
        LogInfo(msg=['Robot description semantic: ', 
                    str(moveit_config.robot_description_semantic)]),
        generate_demo_launch(moveit_config)
    ])
