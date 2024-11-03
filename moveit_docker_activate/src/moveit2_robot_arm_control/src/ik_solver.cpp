#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/robot_state/robot_state.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.hpp>
#include <ament_index_cpp/get_package_share_directory.hpp>
#include <sensor_msgs/msg/joint_state.hpp>

class IKSolver : public rclcpp::Node
{
public:
    IKSolver() : Node("ik_solver")
    {
        // 創建關節狀態發布器
        joint_state_publisher_ = this->create_publisher<sensor_msgs::msg::JointState>(
            "ik_joint_states", 10);

        // 初始化 MoveGroup
        move_group_node_ = std::make_shared<rclcpp::Node>(
            "ik_solver_move_group",
            rclcpp::NodeOptions().automatically_declare_parameters_from_overrides(true)
        );

        executor_ = std::make_shared<rclcpp::executors::SingleThreadedExecutor>();
        executor_->add_node(move_group_node_);
        spin_thread_ = std::make_unique<std::thread>([this]() { executor_->spin(); });

        // 初始化 MoveGroup
        static const std::string PLANNING_GROUP = "arm";
        move_group_ = std::make_unique<moveit::planning_interface::MoveGroupInterface>(move_group_node_, PLANNING_GROUP);

        // 打印機器人信息
        RCLCPP_INFO(this->get_logger(), "Planning frame: %s", move_group_->getPlanningFrame().c_str());
        RCLCPP_INFO(this->get_logger(), "End effector link: %s", move_group_->getEndEffectorLink().c_str());

        // 設置一個測試位姿
        test_ik();
    }

    ~IKSolver()
    {
        if (spin_thread_) {
            executor_->cancel();
            spin_thread_->join();
        }
    }

private:
    void test_ik()
    {
        // 設置目標位姿
        geometry_msgs::msg::Pose target_pose;
        target_pose.position.x = 0.3;
        target_pose.position.y = 0.0;
        target_pose.position.z = 0.3;
        
        target_pose.orientation.w = 1.0;
        target_pose.orientation.x = 0.0;
        target_pose.orientation.y = 0.0;
        target_pose.orientation.z = 0.0;

        // 打印目標位姿
        RCLCPP_INFO(this->get_logger(), "Target pose:");
        RCLCPP_INFO(this->get_logger(), "Position: x=%.3f, y=%.3f, z=%.3f",
            target_pose.position.x, target_pose.position.y, target_pose.position.z);
        RCLCPP_INFO(this->get_logger(), "Orientation: w=%.3f, x=%.3f, y=%.3f, z=%.3f",
            target_pose.orientation.w, target_pose.orientation.x,
            target_pose.orientation.y, target_pose.orientation.z);

        move_group_->setPoseTarget(target_pose);

        // 嘗試求解 IK
        moveit::planning_interface::MoveGroupInterface::Plan my_plan;
        bool success = (move_group_->plan(my_plan) == moveit::core::MoveItErrorCode::SUCCESS);

        if (success)
        {
            auto trajectory = my_plan.trajectory_.joint_trajectory;
            auto joint_positions = trajectory.points.back().positions;
            auto joint_names = trajectory.joint_names;

            // 創建並填充 JointState 消息
            auto joint_state_msg = sensor_msgs::msg::JointState();
            joint_state_msg.header.stamp = this->now();
            joint_state_msg.name = joint_names;
            joint_state_msg.position = joint_positions;

            // 發布關節狀態
            joint_state_publisher_->publish(joint_state_msg);

            // 打印關節角度
            RCLCPP_INFO(this->get_logger(), "IK solution found:");
            for (size_t i = 0; i < joint_names.size(); ++i) {
                RCLCPP_INFO(this->get_logger(), "%s: %.3f degrees (%.3f radians)", 
                    joint_names[i].c_str(), 
                    joint_positions[i] * 180.0 / M_PI,  // 轉換為角度
                    joint_positions[i]);                 // 弧度值
            }
        }
        else
        {
            RCLCPP_ERROR(this->get_logger(), "No IK solution found");
        }
    }

    rclcpp::Node::SharedPtr move_group_node_;
    std::shared_ptr<rclcpp::executors::SingleThreadedExecutor> executor_;
    std::unique_ptr<std::thread> spin_thread_;
    std::unique_ptr<moveit::planning_interface::MoveGroupInterface> move_group_;
    rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr joint_state_publisher_;
};

int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<IKSolver>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
