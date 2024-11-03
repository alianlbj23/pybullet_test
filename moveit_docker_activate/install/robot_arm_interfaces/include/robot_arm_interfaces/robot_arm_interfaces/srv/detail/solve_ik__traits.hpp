// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_arm_interfaces:srv/SolveIK.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__TRAITS_HPP_
#define ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robot_arm_interfaces/srv/detail/solve_ik__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robot_arm_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SolveIK_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: z
  {
    out << "z: ";
    rosidl_generator_traits::value_to_yaml(msg.z, out);
    out << ", ";
  }

  // member: roll
  {
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << ", ";
  }

  // member: pitch
  {
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << ", ";
  }

  // member: yaw
  {
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SolveIK_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: z
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "z: ";
    rosidl_generator_traits::value_to_yaml(msg.z, out);
    out << "\n";
  }

  // member: roll
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "roll: ";
    rosidl_generator_traits::value_to_yaml(msg.roll, out);
    out << "\n";
  }

  // member: pitch
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pitch: ";
    rosidl_generator_traits::value_to_yaml(msg.pitch, out);
    out << "\n";
  }

  // member: yaw
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "yaw: ";
    rosidl_generator_traits::value_to_yaml(msg.yaw, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SolveIK_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_arm_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robot_arm_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_arm_interfaces::srv::SolveIK_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_arm_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_arm_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_arm_interfaces::srv::SolveIK_Request & msg)
{
  return robot_arm_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_arm_interfaces::srv::SolveIK_Request>()
{
  return "robot_arm_interfaces::srv::SolveIK_Request";
}

template<>
inline const char * name<robot_arm_interfaces::srv::SolveIK_Request>()
{
  return "robot_arm_interfaces/srv/SolveIK_Request";
}

template<>
struct has_fixed_size<robot_arm_interfaces::srv::SolveIK_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_arm_interfaces::srv::SolveIK_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_arm_interfaces::srv::SolveIK_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace robot_arm_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const SolveIK_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: joint_positions
  {
    if (msg.joint_positions.size() == 0) {
      out << "joint_positions: []";
    } else {
      out << "joint_positions: [";
      size_t pending_items = msg.joint_positions.size();
      for (auto item : msg.joint_positions) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SolveIK_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }

  // member: joint_positions
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.joint_positions.size() == 0) {
      out << "joint_positions: []\n";
    } else {
      out << "joint_positions:\n";
      for (auto item : msg.joint_positions) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SolveIK_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_arm_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robot_arm_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_arm_interfaces::srv::SolveIK_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_arm_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_arm_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_arm_interfaces::srv::SolveIK_Response & msg)
{
  return robot_arm_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_arm_interfaces::srv::SolveIK_Response>()
{
  return "robot_arm_interfaces::srv::SolveIK_Response";
}

template<>
inline const char * name<robot_arm_interfaces::srv::SolveIK_Response>()
{
  return "robot_arm_interfaces/srv/SolveIK_Response";
}

template<>
struct has_fixed_size<robot_arm_interfaces::srv::SolveIK_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_arm_interfaces::srv::SolveIK_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_arm_interfaces::srv::SolveIK_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_arm_interfaces::srv::SolveIK>()
{
  return "robot_arm_interfaces::srv::SolveIK";
}

template<>
inline const char * name<robot_arm_interfaces::srv::SolveIK>()
{
  return "robot_arm_interfaces/srv/SolveIK";
}

template<>
struct has_fixed_size<robot_arm_interfaces::srv::SolveIK>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_arm_interfaces::srv::SolveIK_Request>::value &&
    has_fixed_size<robot_arm_interfaces::srv::SolveIK_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_arm_interfaces::srv::SolveIK>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_arm_interfaces::srv::SolveIK_Request>::value &&
    has_bounded_size<robot_arm_interfaces::srv::SolveIK_Response>::value
  >
{
};

template<>
struct is_service<robot_arm_interfaces::srv::SolveIK>
  : std::true_type
{
};

template<>
struct is_service_request<robot_arm_interfaces::srv::SolveIK_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_arm_interfaces::srv::SolveIK_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__TRAITS_HPP_
