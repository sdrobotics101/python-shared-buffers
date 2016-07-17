from ctypes import *

class AxisControl(Union):
    _fields_ = [
               ("vel", c_double * 1),
               ("pos", c_float  * 2)
               ]

class ControlInput(Structure):
    _fields_ = [
               ("angular", AxisControl * 3),
               ("linear",  AxisControl * 3),
               ("mode",    c_uint8     * 1)
               ]

class Kill(Structure):
    _fields_ = [
               ("isKilled", c_bool * 1)
               ]

class Health(Structure):
    _fields_= [
              ("saturated", c_uint8 * 1),
              ("direction", c_uint8 * 1)
              ]
