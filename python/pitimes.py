#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

printer.boldOn()
printer.println("Cook County commissioners approve 2018 budget with over 300 layoffs")
printer.boldOff()

printer.println("CHICAGO - The Cook County commissioners unanimously passed the 2018 budget Tuesday, cutting $200 million and over 300 jobs in the process.")

printer.feed(4)
