from ctypes import Structure, c_double, c_uint8, c_char


class Detection(Structure):
    _fields_ = [
        ("x", c_double),
        ("y", c_double),
        ("w", c_double),
        ("h", c_double),
        ("size", c_double),
        ("cls", c_uint8),
    ]

class DetectionArray(Structure):
    _fields_ = [("detections", Detection * 8)]
