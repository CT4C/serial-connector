import serial
import codecs
import argparse
import threading
import sys

OUT_FILE = "serial_output.txt"

parser = argparse.ArgumentParser(prog="serial-debug")

parser.add_argument("-p", "--port", required=True,
                    help="Target port, Ex: /dev/ttyUSB0", default="/dev/ttyUSB0")
parser.add_argument("-b", "--baud", required=False,
                    default=int(9600), help="Baud Rate")
parser.add_argument("-S", "--stop", required=False,
                    default=int(1), help=f"Stop Bit {serial.STOPBITS_ONE}")
parser.add_argument("-P", "--parity", required=False,
                    default=serial.PARITY_NONE, help="Parity Bit")
parser.add_argument("-B", "--byte-size", required=False,
                    default=int(8), help="Byte Size")
parser.add_argument("-t", "--read-timeout", required=False,
                    default=int(5), help="Read Timeout")
parser.add_argument("-r", "--read-exact", required=False,
                    default=int(8), help="Read exact amount of bytes")
parser.add_argument("-d", "--decode", required=False, default="utf-8",
                    help="Decode to exact encoding, leave empty string to skip")
parser.add_argument("-o", "--output", required=False, default="file",
                    help="Output to file or stdout. If file is chosen, encodings are restricted")


config = parser.parse_args()

port_name = config.port
baud = int(config.baud)
stop = int(config.stop)
parity = config.parity
timeout = int(config.read_timeout)
read_exact = int(config.read_exact)
byte_size = int(config.byte_size)
decode = config.decode
output = config.output


class Writer:
    def write(__s: str) -> int:
        pass


def read_serial(port: serial.Serial, writer: Writer):
    while True:
        data = port.read(read_exact)
        port.flush()

        if len(decode) > 0:
            data = codecs.decode(data, decode)

        if len(data) > 0:
            writer.write(data)


def stdin_to_serial(serial: serial.Serial):
    while True:
        data = sys.stdin.read()

        if len(data) > 0:
            serial.write(bytes(data))


def preset_writing_and_listen(port: serial.Serial):
    print(f"Type data to write to serial port {port_name}")
    stdin_to_serial(port)


try:
    port = serial.Serial(port=port_name, baudrate=baud,
                         stopbits=stop, parity=parity, bytesize=byte_size)

    port.timeout = timeout

    out = None

    if output == "file":
        out = open(OUT_FILE, "a+", buffering=1)
    else:
        out = sys.stdout

    read_worker = threading.Thread(target=read_serial, args=[port, out])
    write_worker = threading.Thread(target=preset_writing_and_listen, args=[port])

    '''
        One thread blocks other one - weird
    '''
    read_worker.run()
    write_worker.run()

    read_worker.join()
    write_worker.join()
except Exception as e:
    print(e)
