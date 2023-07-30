import sys

from serial_connector.constants import *
from serial_connector.interfaces import Writer

def create_output(mode: str) -> Writer:
    out = None
    if mode == MODE_DIST:
        out = open(OUT_FILE, "w+", buffering=1)
    if mode == MODE_SHELL:
        out = sys.stdout
    if mode == MODE_ONLY_OUT:
        out = sys.stdout
    return out
