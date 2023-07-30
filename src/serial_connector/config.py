import argparse
import cli


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
        self.port = flags[cli.FLAG_PORT]
        self.baud = int(flags[cli.FLAG_BAUD])
        self.stop = int(flags[cli.FLAG_STOP])
        self.mode = flags[cli.FLAG_MODE]
        self.parity = flags[cli.FLAG_PARITY]
        self.decode = flags[cli.FLAG_DECODE]
        self.byte_size = int(flags[cli.FLAG_BYTE_SIZE])
        self.read_exact = int(flags[cli.FLAG_READ_EXACT])
        self.read_timeout = int(flags[cli.FLAG_READ_TIMEOUT])

    