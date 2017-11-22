#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
line = " ".join(sys.argv[1:])

printer.println(line)
printer.feed(4)
