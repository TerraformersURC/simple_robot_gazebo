# Launches start_world, spawn_simple_robot, 
# and urdf_visualize_control in order with 1
# second in between each launch.
# Timer may not be needed


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_gazebo = get_package_share_directory('simple_robot_gazebo')
    pkg_description = get_package_share_directory('simple_robot_description')

    start_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            pkg_gazebo + '/launch/start_world.launch.py'
        )
    )

    spawn_robot = TimerAction(
        period=1.0,  # wait 1 seconds after start_world
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    pkg_gazebo + '/launch/spawn_simple_robot.launch.py'
                )
            )
        ]
    )

    visualize = TimerAction(
        period=2.0,  # wait 2 seconds after start_world
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    pkg_description + '/launch/urdf_visualize_control.launch.py'
                )
            )
        ]
    )

    return LaunchDescription([start_world, spawn_robot, visualize])
