from ctypes import Structure, c_double, c_uint8, c_char


class Detection(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double),
        ("size", c_uint8),
        ("type", c_uint8),
    ]

class DetectionArray(Structure):
    _fields_ = [("detections", Detection * 8)]
