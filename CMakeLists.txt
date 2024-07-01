cmake_minimum_required(VERSION 3.8)
project(robotie)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(vel_publisher src/vel_publisher.cpp)
ament_target_dependencies(vel_publisher rclcpp geometry_msgs)

install(TARGETS
  vel_publisher 
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY 
  launch description config
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
