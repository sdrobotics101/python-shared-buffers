from ctypes import *

class Location(Structure):
    _fields_ = [
               ("x", c_double * 1),
               ("y", c_double * 1),
               ("z", c_double * 1),
               ]
