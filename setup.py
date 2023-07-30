#!/usr/bin/env python3
from distutils.core import setup

def read(path: str) -> str:
    with open(path) as f:
        return f.read()
    
def read_lines(path: str):
    with open(path) as f:
        return f.readlines()
    

setup(
    name="serial-connector",
    version="0.0.1",
    author="Dmytro Prykhodko",
    author_email="edpryk@gmail.com",
    packages=["serial_connector"],
    keywords=["serial", "debug", "communication"],
    download_url="https://github.com/edpryk/serial-connector",
    package_dir={"": "src"},
    description="Communicate with a serial port",
    license="MIT",
    url="https://github.com/edpryk/serial-connector",
    entry_points = {
        "console_scripts": [
            "serial_connector=serial_connector.main:main"
        ]
    },
    long_description=read("README.md"),
    requires=read_lines("requirements.txt") ,
)
