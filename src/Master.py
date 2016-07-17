from ctypes import *

class Goals(Structure):
    _fields_ = [
               ("forwardVision", c_uint8 * 1),
               ("downVision",    c_uint8 * 1),
               ("sonar",         c_uint8 * 1),
               ]

class SensorReset(Structure):
    _fields_ = [
               ("pos",   c_double * 3),
               ("reset", c_bool   * 1)
               ]
