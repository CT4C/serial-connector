from interfaces import Reader, Writer

class User:
    def __init__(self, port):
        self.port = port

    def listen_input(self, src: Reader, dst: Writer):
        print(f"[+] Type data, press `Ctrl+D` to send to {self.port}")
        while True:
            data = src.read()
            dst.write(data)