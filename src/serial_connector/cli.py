import argparse
import serial

from serial_connector.constants import *

### Docs
parser = argparse.ArgumentParser(prog="serial-connector")

parser.add_argument("-p", f"--{FLAG_PORT}", required=False,
                    help="Target port, Example: /dev/ttyUSB0", default="/dev/ttyUSB0")
parser.add_argument("-b", f"--{FLAG_BAUD}", required=False,
                    default=9600, help="Baud Rate")
parser.add_argument("-m", f"--{FLAG_MODE}", required=False,
                    default=MODE_DIST, help="Mode", choices=[MODE_SHELL, MODE_DIST, MODE_ONLY_OUT])
parser.add_argument("-S", f"--{FLAG_STOP}", required=False,
                    default=int(1), help=f"Stop Bit")
parser.add_argument("-P", f"--{FLAG_PARITY}", required=False, choices=[serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO],
                    default=serial.PARITY_NONE, help="Parity Bit")
parser.add_argument("-B", f"--{FLAG_BYTE_SIZE}", required=False,
                    default=8, help="Byte Size")
parser.add_argument("-t", f"--{FLAG_READ_TIMEOUT}", required=False,
                    default=int(5), help="Read Timeout")
parser.add_argument("-r", f"--{FLAG_READ_EXACT}", required=False,
                    default=int(8), help="Read exact amount of bytes")
parser.add_argument("-d", f"--{FLAG_DECODE}", required=False, default="utf-8",
                    help="Decode to exact encoding, leave empty string to skip")

flags = parser.parse_args()
