from ctypes import *

# converts a ctype into a string
def Pack(ctype_instance):
    return string_at(addressof(ctype_instance), sizeof(ctype_instance)).decode('latin1')

# convert from string to ctype
def Unpack(ctype, string):
    buf = string.encode('latin1')
    cstring = create_string_buffer(buf)
    ctype_instance = cast(pointer(cstring), POINTER(ctype)).contents
    return ctype_instance
