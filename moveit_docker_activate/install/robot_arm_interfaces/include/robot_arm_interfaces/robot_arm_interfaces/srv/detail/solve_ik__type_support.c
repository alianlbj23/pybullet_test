// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_arm_interfaces:srv/SolveIK.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_arm_interfaces/srv/detail/solve_ik__rosidl_typesupport_introspection_c.h"
#include "robot_arm_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_arm_interfaces/srv/detail/solve_ik__functions.h"
#include "robot_arm_interfaces/srv/detail/solve_ik__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_arm_interfaces__srv__SolveIK_Request__init(message_memory);
}

void robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_fini_function(void * message_memory)
{
  robot_arm_interfaces__srv__SolveIK_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_member_array[6] = {
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Request, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Request, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Request, z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "roll",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Request, roll),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pitch",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Request, pitch),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yaw",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Request, yaw),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_members = {
  "robot_arm_interfaces__srv",  // message namespace
  "SolveIK_Request",  // message name
  6,  // number of fields
  sizeof(robot_arm_interfaces__srv__SolveIK_Request),
  robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_member_array,  // message members
  robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_type_support_handle = {
  0,
  &robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_arm_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK_Request)() {
  if (!robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_type_support_handle.typesupport_identifier) {
    robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_arm_interfaces__srv__SolveIK_Request__rosidl_typesupport_introspection_c__SolveIK_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_arm_interfaces/srv/detail/solve_ik__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_arm_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_arm_interfaces/srv/detail/solve_ik__functions.h"
// already included above
// #include "robot_arm_interfaces/srv/detail/solve_ik__struct.h"


// Include directives for member types
// Member `joint_positions`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_arm_interfaces__srv__SolveIK_Response__init(message_memory);
}

void robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_fini_function(void * message_memory)
{
  robot_arm_interfaces__srv__SolveIK_Response__fini(message_memory);
}

size_t robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__size_function__SolveIK_Response__joint_positions(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__get_const_function__SolveIK_Response__joint_positions(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__get_function__SolveIK_Response__joint_positions(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__fetch_function__SolveIK_Response__joint_positions(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__get_const_function__SolveIK_Response__joint_positions(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__assign_function__SolveIK_Response__joint_positions(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__get_function__SolveIK_Response__joint_positions(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__resize_function__SolveIK_Response__joint_positions(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_member_array[3] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "joint_positions",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Response, joint_positions),  // bytes offset in struct
    NULL,  // default value
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__size_function__SolveIK_Response__joint_positions,  // size() function pointer
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__get_const_function__SolveIK_Response__joint_positions,  // get_const(index) function pointer
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__get_function__SolveIK_Response__joint_positions,  // get(index) function pointer
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__fetch_function__SolveIK_Response__joint_positions,  // fetch(index, &value) function pointer
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__assign_function__SolveIK_Response__joint_positions,  // assign(index, value) function pointer
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__resize_function__SolveIK_Response__joint_positions  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_arm_interfaces__srv__SolveIK_Response, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_members = {
  "robot_arm_interfaces__srv",  // message namespace
  "SolveIK_Response",  // message name
  3,  // number of fields
  sizeof(robot_arm_interfaces__srv__SolveIK_Response),
  robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_member_array,  // message members
  robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_type_support_handle = {
  0,
  &robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_arm_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK_Response)() {
  if (!robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_type_support_handle.typesupport_identifier) {
    robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_arm_interfaces__srv__SolveIK_Response__rosidl_typesupport_introspection_c__SolveIK_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_arm_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_arm_interfaces/srv/detail/solve_ik__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_members = {
  "robot_arm_interfaces__srv",  // service namespace
  "SolveIK",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_Request_message_type_support_handle,
  NULL  // response message
  // robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_Response_message_type_support_handle
};

static rosidl_service_type_support_t robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_type_support_handle = {
  0,
  &robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_arm_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK)() {
  if (!robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_type_support_handle.typesupport_identifier) {
    robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_arm_interfaces, srv, SolveIK_Response)()->data;
  }

  return &robot_arm_interfaces__srv__detail__solve_ik__rosidl_typesupport_introspection_c__SolveIK_service_type_support_handle;
}
