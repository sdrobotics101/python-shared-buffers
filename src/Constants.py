SENSORS_LINEAR = "linear"
SENSORS_ANGULAR = "angular"
SENSORS_DATA = "data"
MOTOR_HEALTH = "health"
MOTOR_KILL = "kill"
MOTOR_OUTPUTS = "outputs"
TARGET_LOCATION = "targetlocation"
TARGET_LOCATION_AND_ROTATION = "targetLocAndRot"
MASTER_CONTROL = "control"
MASTER_GOALS = "goals"
MASTER_SENSOR_RESET = "sensorreset"

MASTER_SERVER_ID = 42
SENSOR_SERVER_ID = 43
MOTOR_SERVER_ID = 44
FORWARD_VISION_SERVER_ID = 45
DOWNWARD_VISION_SERVER_ID = 46
SONAR_SERVER_ID = 47

MASTER_SERVER_IP = "10.0.0.42"
SENSOR_SERVER_IP = "10.0.0.43"
MOTOR_SERVER_IP = "10.0.0.44"
FORWARD_VISION_SERVER_IP = "10.0.0.45"
DOWNWARD_VISION_SERVER_IP = "10.0.0.46"
SONAR_SERVER_IP = "10.0.0.47"

# axes
xaxis = 0
yaxis = 1
zaxis = 2

# quaternion
QUAT_W = 0
QUAT_X = 1
QUAT_Y = 2
QUAT_Z = 3

# angular values
POSITION = 0
TIME = 1

# Location.type
NONE = 0
RED = 1
YELLOW = 2
GREEN = 3
GATEPOLE = 4

# goal types
GOAL_NONE = 0
GOAL_FIND_GATE = 1
GOAL_FIND_RED_BUOY = 2
GOAL_FIND_YELLOW_BUOY = 3
GOAL_FIND_GREEN_BUOY = 4
GOAL_FIND_PATH = 5