from typing import List
import threading
import sys


from cli import flags, MODE_ONLY_OUT
from connector import Connector
from config import Config
from output import create_output
from user import User

threads: List[threading.Thread] = []
config = Config(vars(flags))
out = create_output(config.mode)
connector = Connector(config)
user = User(config.port)

err = connector.connect()
if err != None:
    print("[-] " + err)
    sys.exit(1)


read_serial_thread = threading.Thread(
    target=connector.read,
    args=[out],
    name="SerialRead"
)
read_serial_thread.daemon = True
read_serial_thread.start()
threads.append(read_serial_thread)

if not config.mode == MODE_ONLY_OUT:
    write_serial_thread = threading.Thread(
        target=user.listen_input,
        args=[sys.stdin, out],
        name="SerialWrite"
    )
    write_serial_thread.daemon = True
    write_serial_thread.start()
    threads.append(write_serial_thread)

for thread in threads:
    print(f"[+] {thread.name} started")
    thread.join()
