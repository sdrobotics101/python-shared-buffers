from ctypes import c_bool, c_double, c_uint8, c_uint16, Structure

class Kill(Structure):
    _fields_ = [("isKilled", c_bool)]

class Health(Structure):
    _fields_ = [("saturated", c_uint8), ("direction", c_uint8)]

class Outputs(Structure):
    _fields_ = [("motors", c_double * 8)]

class RawOutputs(Structure):
    _fields_ = [("motors", c_uint16 * 8)]

class PhysicalOutput(Structure):
    _fields_ = [("force", c_double * 3), ("torque", c_double * 3)]

class DropperOutput(Structure):
    _fields_ = [("droppers", c_bool * 2)]
