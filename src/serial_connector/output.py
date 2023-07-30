import sys

from cli import MODE_DIST, MODE_ONLY_OUT, MODE_SHELL
from interfaces import Writer
from constants import OUT_FILE

def create_output(mode: str) -> Writer:
    out = None
    if mode == MODE_DIST:
        out = open(OUT_FILE, "w+", buffering=1)
    if mode == MODE_SHELL:
        out = sys.stdout
    if mode == MODE_ONLY_OUT:
        out = sys.stdout
    return out
