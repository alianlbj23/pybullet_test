import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/user/workspace/pyrobot/moveit_docker_activate/install/pros_car_py'
