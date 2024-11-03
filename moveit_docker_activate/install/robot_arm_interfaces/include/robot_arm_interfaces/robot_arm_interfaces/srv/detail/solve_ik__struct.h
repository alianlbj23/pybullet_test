// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_arm_interfaces:srv/SolveIK.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__STRUCT_H_
#define ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/SolveIK in the package robot_arm_interfaces.
typedef struct robot_arm_interfaces__srv__SolveIK_Request
{
  double x;
  double y;
  double z;
  double roll;
  double pitch;
  double yaw;
} robot_arm_interfaces__srv__SolveIK_Request;

// Struct for a sequence of robot_arm_interfaces__srv__SolveIK_Request.
typedef struct robot_arm_interfaces__srv__SolveIK_Request__Sequence
{
  robot_arm_interfaces__srv__SolveIK_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_arm_interfaces__srv__SolveIK_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'joint_positions'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SolveIK in the package robot_arm_interfaces.
typedef struct robot_arm_interfaces__srv__SolveIK_Response
{
  bool success;
  rosidl_runtime_c__double__Sequence joint_positions;
  rosidl_runtime_c__String message;
} robot_arm_interfaces__srv__SolveIK_Response;

// Struct for a sequence of robot_arm_interfaces__srv__SolveIK_Response.
typedef struct robot_arm_interfaces__srv__SolveIK_Response__Sequence
{
  robot_arm_interfaces__srv__SolveIK_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_arm_interfaces__srv__SolveIK_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_ARM_INTERFACES__SRV__DETAIL__SOLVE_IK__STRUCT_H_
