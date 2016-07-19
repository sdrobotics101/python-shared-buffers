from ctypes import *

class Location(Structure):
    _fields_ = [
               ("x", c_double),
               ("y", c_double),
               ("z", c_double),
               ("confidence", c_char),
               ]
