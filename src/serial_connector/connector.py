import codecs
import serial

from interfaces import Writer
from config import Config


class Connector:
    def __init__(self, config: Config):
        self.port: serial.Serial = None
        self.config = config

    def connect(self) -> Exception:
        c = self.config

        try:
          self.port = serial.Serial(port=c.port, baudrate=c.baud,
                          stopbits=c.stop, parity=c.parity, bytesize=c.byte_size)
          
          self.port.timeout = c.read_timeout

          print(f"[+] Connection established: {c.port}")
          print(f"[+] Mode: {c.mode}")
        except Exception:
            return Exception


    def read(self, writer: Writer):
        c = self.config
        
        while True:
            data = self.port.read(c.read_exact)
            self.port.flush()

            if len(c.decode) > 0:
                data = codecs.decode(data, c.decode)

            if len(data) > 0:
                writer.write(data)


    def write(self, data: str):
        if len(data) > 0:
            self.port.write(data.encode())
