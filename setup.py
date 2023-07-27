#!/usr/bin/env python3
from distutils.core import setup

setup(
    name="sdebug",
    version="0.0.1",
    author="Dmytro Prykhodko",
    author_email="edpryk@gmail.com",
    packages=["serial_debug"],
    keywords=["serial", "debug", "communication"],
    download_url="https://github.com/edpryk/serial-debug",
    package_dir={"serial_debug": "src/serial_debug"},
    description="Read serial port and write output either to the `serial_output.txt` or `stdout` User can write data to a serial port through typing it to the `stdin`"
)
