from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()
    
    use_sim_time = LaunchConfiguration('use_sim_time')

    pkg_path = os.path.join(get_package_share_directory('robotie'))
    xacro_file = os.path.join(pkg_path,'description','robotie.xacro')
    robot_description_config = Command(['xacro ', xacro_file, ' sim_mode:=', use_sim_time])
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}

    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_config, 'use_sim_time': use_sim_time}]
    )
    declare_args = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false'
    )

    ld.add_action(rsp_node)
    ld.add_action(declare_args)

    return ld