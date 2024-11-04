# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch.actions import LogInfo, OpaqueFunction
# from launch_ros.actions import Node
# from moveit_configs_utils import MoveItConfigsBuilder
# from moveit_configs_utils.launches import generate_move_group_launch

# def check_files_and_folders(context, *args, **kwargs):
#     urdf_package_path = get_package_share_directory("robot_description_version2")
#     config_package_path = get_package_share_directory("origin_arm")
    
#     urdf_folder = os.path.join(urdf_package_path, "urdf")
#     urdf_file = os.path.join(urdf_folder, "target.urdf")
#     config_folder = os.path.join(config_package_path, "config")
#     srdf_file = os.path.join(config_folder, "angle_excurate_arm_ver2.srdf")

#     if not os.path.isdir(urdf_folder):
#         print(f"[ERROR] URDF folder not found: {urdf_folder}")
#         return [LogInfo(msg=f"[ERROR] URDF folder not found: {urdf_folder}")]
#     if not os.path.isfile(urdf_file):
#         print(f"[ERROR] URDF file not found: {urdf_file}")
#         return [LogInfo(msg=f"[ERROR] URDF file not found: {urdf_file}")]
#     if not os.path.isdir(config_folder):
#         print(f"[ERROR] Config folder not found: {config_folder}")
#         return [LogInfo(msg=f"[ERROR] Config folder not found: {config_folder}")]
#     if not os.path.isfile(srdf_file):
#         print(f"[ERROR] SRDF file not found: {srdf_file}")
#         return [LogInfo(msg=f"[ERROR] SRDF file not found: {srdf_file}")]

#     print("[INFO] All necessary folders and files exist.")
#     return [LogInfo(msg="[INFO] All necessary folders and files exist.")]

# def generate_launch_description():
#     file_and_folder_check_action = OpaqueFunction(function=check_files_and_folders)

#     # 建立 MoveIt 配置
#     moveit_config = MoveItConfigsBuilder(
#         robot_name="angle_excurate_arm_ver2",
#         package_name="origin_arm"
#     ).to_moveit_configs()

#     # 啟動 move_group（MoveIt 控制）
#     move_group_node = generate_move_group_launch(moveit_config)

#     # 啟動 Rviz，並加載 MoveIt 配置
#     rviz_node = Node(
#         package="rviz2",
#         executable="rviz2",
#         name="rviz2",
#         output="screen",
#         arguments=["-d", os.path.join(get_package_share_directory("origin_arm"), "config", "moveit.rviz")],
#         parameters=[moveit_config.to_dict()]
#     )

#     return LaunchDescription([
#         file_and_folder_check_action,
#         move_group_node,
#         rviz_node
#     ])
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("angle_excurate_arm_ver2", package_name="origin_arm").to_moveit_configs()
    return generate_demo_launch(moveit_config)
