#!/usr/bin/env python3
from distutils.core import setup

setup(
    name="sdebug",
    version="1.0",
    author="Dmytro Prykhodko",
    author_email="edpryk@gmaill.com.main",
    packages=["serial_debug"],
    description="Read serial port and write output either to the `serial_output.txt` or `stdout` User can write data to a serial port through typing it to the `stdin`"
)
