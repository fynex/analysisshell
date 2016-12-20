import struct

# TODO
def to_littleendian32(num):
    return struct.pack("<I",num)


def to_littleendian64(num):
    return struct.pack("<Q", num)


def to_hexescaped(data):
    x = format(data, "x")

    return "".join(r"\x" + x[i:i+2].zfill(2) for i in range(0, len(x), 2))


def to_hexescaped_reversed(data):
    s = to_hexescaped(data)

    return "\\x" + "\\x".join([e for e in reversed(s.split("\\x")) if e])

