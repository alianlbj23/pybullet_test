from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_spawn_controllers_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("angle_excurate_arm_ver2", package_name="new_config2").to_moveit_configs()
    return generate_spawn_controllers_launch(moveit_config)
