import argparse
from  serial_connector.constants import *


class Config:
    port: str
    baud: int
    stop: int
    mode: str
    parity: str
    decode: str
    byte_size: int
    read_exact: int
    read_timeout: int

    def __init__(self, flags: argparse.Namespace):
        self.port = flags[FLAG_PORT]
        self.baud = int(flags[FLAG_BAUD])
        self.stop = int(flags[FLAG_STOP])
        self.mode = flags[FLAG_MODE]
        self.parity = flags[FLAG_PARITY]
        self.decode = flags[FLAG_DECODE]
        self.byte_size = int(flags[FLAG_BYTE_SIZE])
        self.read_exact = int(flags[FLAG_READ_EXACT])
        self.read_timeout = int(flags[FLAG_READ_TIMEOUT])

    