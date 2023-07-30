# Serial Port Connector

## Installation
```
pip install git+https://github.com/edpryk/serial-connector
```
---


## Description
CLI tool to communicate with a serial port.\
Three modes can be used:
- `dist` serial output will be routed to the `serial_output.txt`, user can send data through the `stdin` 
- `shell` serial output will be routed to the `stdout`, user can send data through the `stdin`
- `only-out` serial output will be routed to the `stdout`
  
## Manual:
```
usage: serialc [-h] [-p PORT] [-b BAUD] [-m {shell,dist,only-out}] [-S STOP] [-P {1,1.5,2}] [-B BYTE_SIZE] [-t READ_TIMEOUT] [-r READ_EXACT] [-d DECODE]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Target port, Example: /dev/ttyUSB0
  -b BAUD, --baud BAUD  Baud Rate
  -m {shell,dist,only-out}, --mode {shell,dist,only-out}
                        Mode
  -S STOP, --stop STOP  Stop Bit 1
  -P {1,1.5,2}, --parity {1,1.5,2}
                        Parity Bit
  -B BYTE_SIZE, --byte-size BYTE_SIZE
                        Byte Size
  -t READ_TIMEOUT, --read-timeout READ_TIMEOUT
                        Read Timeout
  -r READ_EXACT, --read_exact READ_EXACT
                        Read exact amount of bytes
  -d DECODE, --decode DECODE
                        Decode to exact encoding, leave empty string to skip
```

> Press  `Ctrl+D` to send data.
---


### Summary

- Written to communicate with `AVR boards`
- Tested with the `atmega328p`

---