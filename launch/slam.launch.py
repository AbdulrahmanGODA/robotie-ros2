import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    package_name = 'robotie'
    rsp_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rsp.launch.py')]), launch_arguments={
                'use_sim_time' : 'true'
            }.items()
    )
    gazebo_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')])
    )
    slam_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py')])
    )
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'rrbot'],
        output='screen'
    )
    launch_rviz2 = ExecuteProcess(
        cmd=[['rviz2']],
        shell=True
    )
    diff_drive_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_cont']
    )
    joint_broad_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_broad']
    )
    ld.add_action(rsp_include)
    ld.add_action(gazebo_include)
    ld.add_action(spawn_entity)
    ld.add_action(launch_rviz2)
    ld.add_action(diff_drive_spawner)
    ld.add_action(joint_broad_spawner)
    ld.add_action(slam_include)

    return ld

