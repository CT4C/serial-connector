#!/usr/bin/env python3
from typing import List
import threading
import sys

sys.path.append("~/.local/")


from serial_connector.cli import flags, MODE_ONLY_OUT
from serial_connector.connector import Connector
from serial_connector.config import Config
from serial_connector.output import create_output
from serial_connector.user import User

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
