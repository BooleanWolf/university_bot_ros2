from launch import LaunchDescription 
from launch_ros.actions import Node 


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='varsity_bot', 
                namespace='bot', 
                executable='chatter',
                name='chatter'
            ), 
             Node(
                package='varsity_bot', 
                namespace='bot', 
                executable='main',
                name='main'
            )
        ]
    )