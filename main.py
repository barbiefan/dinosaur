from PIL import ImageGrab
import time
import keyboard
import os
from copy import deepcopy

os.environ["DISPLAY"] = ":0"

x1, x2 = 500,600

COORDS = [
            (x1, 360),
            (x2, 360)
         ]
DISTANCE = x2-x1
DINO = 260


def main():
    queue = []
    while True:
        frame = ImageGrab.grab()
        pixel1 = frame.getpixel(COORDS[0])
        pixel2 = frame.getpixel(COORDS[1])
        if sum(pixel2)/3 < 170:
            queue.append(time.perf_counter())
        if sum(pixel1)/3 < 170:
            velocity = DISTANCE/(time.perf_counter()-queue.pop(0))
            print(velocity)
            
main()
