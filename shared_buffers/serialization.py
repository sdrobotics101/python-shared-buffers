from ctypes import (
    string_at,
    addressof,
    sizeof,
    create_string_buffer,
    cast,
    pointer,
    POINTER,
)

# converts a ctype into a string
def pack(ctype_instance):
    return string_at(addressof(ctype_instance), sizeof(ctype_instance))


# convert from string to ctype
def unpack(ctype, string):
    buf = b""
    for i in string:
        buf += i.to_bytes(1, "little")
    cstring = create_string_buffer(buf)
    ctype_instance = cast(pointer(cstring), POINTER(ctype)).contents
    return ctype_instance
