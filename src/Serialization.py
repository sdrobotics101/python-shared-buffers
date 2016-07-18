from ctypes import *

def Pack(ctype_instance):
    buf = string_at(addressof(ctype_instance), sizeof(ctype_instance))
    string = ''.join([chr(i) for i in buf])
    return string

def Unpack(ctype, string):
    # buf = str.encode(string)
    buf = bytearray()
    buf.extend(map(ord, string))
    cstring = create_string_buffer(buf)
    ctype_instance = cast(pointer(cstring), POINTER(ctype)).contents
    return ctype_instance
