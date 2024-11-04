import os
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch import LaunchDescription
from launch.actions import LogInfo
from launch.actions import OpaqueFunction

def check_files_and_folders(context, *args, **kwargs):
    package_path = "/path/to/origin_arm"  # 替換為你的 package 路徑
    urdf_folder = os.path.join(package_path, "urdf")
    config_folder = os.path.join(package_path, "config")
    urdf_file = os.path.join(urdf_folder, "angle_excurate_arm_ver2.urdf")
    srdf_file = os.path.join(config_folder, "angle_excurate_arm_ver2.srdf")

    # 檢查 URDF 資料夾是否存在
    if not os.path.isdir(urdf_folder):
        print(f"[ERROR] URDF folder not found: {urdf_folder}")
        return []

    # 檢查 URDF 檔案是否存在
    if not os.path.isfile(urdf_file):
        print(f"[ERROR] URDF file not found: {urdf_file}")
        return []

    # 檢查 Config 資料夾是否存在
    if not os.path.isdir(config_folder):
        print(f"[ERROR] Config folder not found: {config_folder}")
        return []

    # 檢查 SRDF 檔案是否存在
    if not os.path.isfile(srdf_file):
        print(f"[ERROR] SRDF file not found: {srdf_file}")
        return []

    print("[INFO] All necessary folders and files exist.")
    return [LogInfo(msg="All necessary folders and files exist.")]

def generate_launch_description():
    # 檢查資料夾和檔案存在性
    file_and_folder_check_action = OpaqueFunction(function=check_files_and_folders)

    # 確認檔案後生成 MoveIt 設定
    moveit_config = MoveItConfigsBuilder(
        "angle_excurate_arm_ver2", 
        package_name="origin_arm"
    ).robot_description_semantic("config/angle_excurate_arm_ver2.srdf").to_moveit_configs()

    return LaunchDescription([
        file_and_folder_check_action,
        generate_demo_launch(moveit_config)
    ])
