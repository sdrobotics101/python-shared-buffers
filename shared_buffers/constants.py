from enum import Enum


class Sensor(Enum):
    LINEAR = "linear"
    ANGULAR = "angular"
    DATA = "data"


class Motor(Enum):
    HEALTH = "health"
    KILL = "kill"
    OUTPUTS = "outputs"


class Vision(Enum):
    FORWARD_DETECTION = "forwarddetection"
    DOWNWARD_DETECTION = "downwarddetection"

class Master(Enum):
    CONTROL = "control"
    GOALS = "goals"
    SENSOR_RESET = "sensorreset"


class ServerID(Enum):
    MASTER_SERVER_ID = 42
    SENSOR_SERVER_ID = 43
    MOTOR_SERVER_ID = 44
    FORWARD_VISION_SERVER_ID = 45
    DOWNWARD_VISION_SERVER_ID = 46
    SONAR_SERVER_ID = 47


class PiIP(Enum):
    MASTER = "10.0.0.42"
    SENSOR = "10.0.0.43"
    MOTOR = "10.0.0.44"
    FORWARD_VISION = "10.0.0.45"
    DOWNWARD_VISION = "10.0.0.46"
    SONAR = "10.0.0.47"


# axes
class Axes(Enum):
    xaxis = 0
    yaxis = 1
    zaxis = 2


# quaternion
class Quaternion(Enum):
    QUAT_W = 0
    QUAT_X = 1
    QUAT_Y = 2
    QUAT_Z = 3


# angular values
POSITION = 0
TIME = 1

# Location.type
class LocationType(Enum):
    NONE = 0
    REDBUOY = 1
    YELLOWBUOY = 2
    GREENBUOY = 3
    GATEPOLE = 4


# goal types
class Goal(Enum):
    NONE = 0
    FIND_GATE = 1
    FIND_RED_BUOY = 2
    FIND_YELLOW_BUOY = 3
    FIND_GREEN_BUOY = 4
    FIND_PATH = 5
    FIND_OCTOGON = 6


# variable confidence level
CONFIDENCE = 128

# depth
DEPTH = 2

# velocity in m/s
VELOCITY = 1

# variable x, y, and z velocities for dead reckoning
XVEL = 3
YVEL = 3
ZVEL = 0
