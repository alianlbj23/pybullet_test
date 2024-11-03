cmake_minimum_required(VERSION 3.22)
project(moveit_robot_generate)

# 使用 C++ 14 標準
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# 找尋必要的依賴包
find_package(ament_cmake REQUIRED)
find_package(moveit_core REQUIRED)
find_package(moveit_ros_planning REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(rclcpp REQUIRED)

# 添加 IK 節點的可執行文件
add_executable(ik_node src/ik_node.cpp)
ament_target_dependencies(ik_node
  rclcpp
  moveit_core
  moveit_ros_planning
  moveit_ros_planning_interface
)

# 安裝可執行文件
install(TARGETS ik_node
  DESTINATION lib/${PROJECT_NAME}
)

# 安裝 launch 文件
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# 安裝配置文件
install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME}
)

# 必須在最後調用這個
ament_package()
