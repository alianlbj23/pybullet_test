from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, FindExecutable
from launch_ros.substitutions import FindPackageShare
import os


def generate_launch_description():
    # 獲取包路徑
    pkg_share = FindPackageShare("moveit_robot_generate").find("moveit_robot_generate")
    
    # 定義配置文件路徑
    urdf_file = os.path.join(pkg_share, "config", "angle_excurate_arm_ver2.urdf.xacro")
    srdf_file = os.path.join(pkg_share, "config", "angle_excurate_arm_ver2.srdf")
    kinematics_file = os.path.join(pkg_share, "config", "kinematics.yaml")
    joint_limits_file = os.path.join(pkg_share, "config", "joint_limits.yaml")
    controllers_file = os.path.join(pkg_share, "config", "ros2_controllers.yaml")
    
    # 啟動 robot_state_publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": urdf_file}]
    )

    # 啟動 joint_state_publisher
    joint_state_publisher = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        output="screen"
    )

    # 啟動 move_group
    move_group = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[{
            "robot_description": urdf_file,
            "robot_description_semantic": srdf_file,
            "robot_description_kinematics": kinematics_file,
            "robot_description_planning": joint_limits_file,
            "controllers_config": controllers_file,
        }]
    )

    # 啟動 RViz
    rviz_config = os.path.join(pkg_share, "config", "moveit.rviz")
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config],
    )

    # 您的 IK 節點
    ik_node = Node(
        package="moveit_robot_generate",
        executable="ik_node",
        name="ik_node",
        output="screen",
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        move_group,
        rviz_node,
        ik_node,
    ])