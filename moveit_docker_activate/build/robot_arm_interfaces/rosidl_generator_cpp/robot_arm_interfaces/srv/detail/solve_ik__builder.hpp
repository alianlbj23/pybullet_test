// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_arm_interfaces:srv/SolveIK.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__BUILDER_HPP_
#define ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_arm_interfaces/srv/detail/solve_ik__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_arm_interfaces
{

namespace srv
{

namespace builder
{

class Init_SolveIK_Request_yaw
{
public:
  explicit Init_SolveIK_Request_yaw(::robot_arm_interfaces::srv::SolveIK_Request & msg)
  : msg_(msg)
  {}
  ::robot_arm_interfaces::srv::SolveIK_Request yaw(::robot_arm_interfaces::srv::SolveIK_Request::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Request msg_;
};

class Init_SolveIK_Request_pitch
{
public:
  explicit Init_SolveIK_Request_pitch(::robot_arm_interfaces::srv::SolveIK_Request & msg)
  : msg_(msg)
  {}
  Init_SolveIK_Request_yaw pitch(::robot_arm_interfaces::srv::SolveIK_Request::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_SolveIK_Request_yaw(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Request msg_;
};

class Init_SolveIK_Request_roll
{
public:
  explicit Init_SolveIK_Request_roll(::robot_arm_interfaces::srv::SolveIK_Request & msg)
  : msg_(msg)
  {}
  Init_SolveIK_Request_pitch roll(::robot_arm_interfaces::srv::SolveIK_Request::_roll_type arg)
  {
    msg_.roll = std::move(arg);
    return Init_SolveIK_Request_pitch(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Request msg_;
};

class Init_SolveIK_Request_z
{
public:
  explicit Init_SolveIK_Request_z(::robot_arm_interfaces::srv::SolveIK_Request & msg)
  : msg_(msg)
  {}
  Init_SolveIK_Request_roll z(::robot_arm_interfaces::srv::SolveIK_Request::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_SolveIK_Request_roll(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Request msg_;
};

class Init_SolveIK_Request_y
{
public:
  explicit Init_SolveIK_Request_y(::robot_arm_interfaces::srv::SolveIK_Request & msg)
  : msg_(msg)
  {}
  Init_SolveIK_Request_z y(::robot_arm_interfaces::srv::SolveIK_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_SolveIK_Request_z(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Request msg_;
};

class Init_SolveIK_Request_x
{
public:
  Init_SolveIK_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SolveIK_Request_y x(::robot_arm_interfaces::srv::SolveIK_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_SolveIK_Request_y(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_arm_interfaces::srv::SolveIK_Request>()
{
  return robot_arm_interfaces::srv::builder::Init_SolveIK_Request_x();
}

}  // namespace robot_arm_interfaces


namespace robot_arm_interfaces
{

namespace srv
{

namespace builder
{

class Init_SolveIK_Response_message
{
public:
  explicit Init_SolveIK_Response_message(::robot_arm_interfaces::srv::SolveIK_Response & msg)
  : msg_(msg)
  {}
  ::robot_arm_interfaces::srv::SolveIK_Response message(::robot_arm_interfaces::srv::SolveIK_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Response msg_;
};

class Init_SolveIK_Response_joint_positions
{
public:
  explicit Init_SolveIK_Response_joint_positions(::robot_arm_interfaces::srv::SolveIK_Response & msg)
  : msg_(msg)
  {}
  Init_SolveIK_Response_message joint_positions(::robot_arm_interfaces::srv::SolveIK_Response::_joint_positions_type arg)
  {
    msg_.joint_positions = std::move(arg);
    return Init_SolveIK_Response_message(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Response msg_;
};

class Init_SolveIK_Response_success
{
public:
  Init_SolveIK_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SolveIK_Response_joint_positions success(::robot_arm_interfaces::srv::SolveIK_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SolveIK_Response_joint_positions(msg_);
  }

private:
  ::robot_arm_interfaces::srv::SolveIK_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_arm_interfaces::srv::SolveIK_Response>()
{
  return robot_arm_interfaces::srv::builder::Init_SolveIK_Response_success();
}

}  // namespace robot_arm_interfaces

#endif  // ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__BUILDER_HPP_
