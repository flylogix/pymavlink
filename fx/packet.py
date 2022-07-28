import struct


def pack(system_id: int, payload: bytes, delimiter: bytes = b"\xba\xda\x55") -> bytes:
    f = ">HH{}s{}s".format(len(payload), len(delimiter))
    return struct.pack(f, len(payload), system_id, payload, delimiter)


def unpack(packet: bytes, delimiter: bytes = b"\xba\xda\x55") -> tuple:
    payload_length = struct.unpack(">H", packet[:2])
    f = ">HH{}s{}s".format(payload_length[0], len(delimiter))
    return struct.unpack(f, packet)
