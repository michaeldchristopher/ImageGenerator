# main.py
# This program is an image generator simulator to test example Golden Image generation for testing VisionTRX
# Michael Christopher
# michael.christopher@ets-lindgren.com
# 
# written in python 3.6.1 (using Anaconda 4.4.0)
# this is provided to our customers for their use

import sys
import tkinter
from PIL import Image


# this class takes command strings and performs those commands
class CommandProcessor:
    def __init__(self):
        print("inside init for CommandProcessor")

    def Perform(self, commandString):
        if commandString == "respond":
            print("i am responding")
            im = Image.open("/Users/Michael/Pictures/koalas.jpeg")
            im.rotate(45).show()
            im.rotate(180 + 45).show()


if __name__ == "__main__":
    cp = CommandProcessor()
    cp.Perform("respond")
    print(sys.version)
