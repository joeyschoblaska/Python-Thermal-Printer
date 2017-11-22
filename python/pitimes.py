#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

def printHeadline(headline):
    printer.boldOn()
    printer.underlineOn()
    printer.println(headline)
    printer.boldOff()
    printer.underlineOff()

printHeadline("Cook County commissioners approve 2018 budget with over 300 layoffs")
printer.println("CHICAGO - The Cook County commissioners unanimously passed the 2018 budget Tuesday, cutting $200 million and over 300 jobs in the process.")

printer.feed(2)

printer.println("The F.C.C. unveiled a plan to repeal net neutrality rules, which require broadband providers to give consumers equal access to all content on the web.")

printer.feed(2)

printer.println("Nancy Pelosi, the House Democratic leader, has called on the Ethics Committee to investigate sexual harassment charges against John Conyers Jr., the House's longest-serving member.")

printer.feed(4)
