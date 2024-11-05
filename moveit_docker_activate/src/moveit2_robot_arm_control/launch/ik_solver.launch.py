from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os
import yaml

config_pkg_name = 'stable_config'
robot_description_pkg_name = "robot_description_version2"

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)
    
    try:
        with open(absolute_file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading yaml: {e}")
        return None

def generate_launch_description():
    # 獲取包的路徑
    moveit_config_pkg = get_package_share_directory(config_pkg_name)
    robot_description_pkg = get_package_share_directory(robot_description_pkg_name)

    # 加載 URDF
    robot_description_path = os.path.join(robot_description_pkg, 'urdf', 'target.urdf')
    with open(robot_description_path, 'r') as file:
        robot_description = file.read()

    # 加載 SRDF
    robot_description_semantic_path = os.path.join(moveit_config_pkg, 'config', 'angle_excurate_arm_ver2.srdf')
    with open(robot_description_semantic_path, 'r') as file:
        robot_description_semantic = file.read()

    # 加載 kinematics.yaml
    kinematics_yaml = load_yaml(config_pkg_name, 'config/kinematics.yaml')
    
    # 加載 joint_limits.yaml
    joint_limits_yaml = load_yaml(config_pkg_name, 'config/joint_limits.yaml')

    # 設置參數
    robot_description_parameters = {
        'robot_description': robot_description,
        'robot_description_semantic': robot_description_semantic,
        'robot_description_kinematics': kinematics_yaml,
        'robot_description_planning': joint_limits_yaml
    }

    # 添加機器人狀態發布器
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # 添加關節狀態發布器
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    # 加載 MoveIt 配置
    moveit_config = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(moveit_config_pkg, 'launch', 'move_group.launch.py')
        )
    )

    # 加載 RViz
    rviz_config = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(moveit_config_pkg, 'launch', 'moveit_rviz.launch.py')
        )
    )

    # 啟動 IK solver 節點
    ik_solver_node = Node(
        package='moveit2_robot_arm_control',
        executable='ik_solver',
        name='ik_solver',
        output='screen',
        parameters=[robot_description_parameters]
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        moveit_config,
        rviz_config,
        ik_solver_node
    ]) 