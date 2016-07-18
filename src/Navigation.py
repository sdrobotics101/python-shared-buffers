from ctypes import *

class Kill(Structure):
    _fields_ = [
               ("isKilled", c_bool)
               ]

class Health(Structure):
    _fields_= [
              ("saturated", c_uint8),
              ("direction", c_uint8)
              ]
