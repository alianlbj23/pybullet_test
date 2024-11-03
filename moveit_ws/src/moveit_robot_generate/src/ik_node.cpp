#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>

int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto const node = std::make_shared<rclcpp::Node>(
        "ik_example",
        rclcpp::NodeOptions().automatically_declare_parameters_from_overrides(true)
    );

    // 使用 ROS2 版本的 MoveGroupInterface
    auto move_group = moveit::planning_interface::MoveGroupInterface(node, "robot_arm");

    // 設定目標位置
    geometry_msgs::msg::Pose target_pose;
    target_pose.orientation.w = 1.0;
    target_pose.position.x = 0.28;
    target_pose.position.y = -0.2;
    target_pose.position.z = 0.5;

    // 設定末端執行器的目標姿態
    move_group.setPoseTarget(target_pose);

    // 進行運動規劃
    moveit::planning_interface::MoveGroupInterface::Plan my_plan;
    auto const success = static_cast<bool>(move_group.plan(my_plan));

    if (success) {
        RCLCPP_INFO(node->get_logger(), "Planning successful!");
        move_group.execute(my_plan);
    } else {
        RCLCPP_ERROR(node->get_logger(), "Planning failed!");
    }

    rclcpp::shutdown();
    return 0;
} 