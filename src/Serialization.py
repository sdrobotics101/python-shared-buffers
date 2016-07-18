from ctypes import *

def Pack(ctype_instance):
    return string_at(addressof(ctype_instance), sizeof(ctype_instance))

def Unpack(ctype, string):
    bytes = str.encode(string)
    cstring = create_string_buffer(bytes)
    ctype_instance = cast(pointer(cstring), POINTER(ctype)).contents
    return ctype_instance
