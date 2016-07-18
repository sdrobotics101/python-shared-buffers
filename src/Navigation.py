from ctypes import *

class Kill(Structure):
    _fields_ = [
               ("isKilled", c_bool * 1)
               ]

class Health(Structure):
    _fields_= [
              ("saturated", c_uint8 * 1),
              ("direction", c_uint8 * 1)
              ]
