from PIL import ImageGrab
import time
import keyboard
import os
from copy import deepcopy

os.environ["DISPLAY"] = ":0"



COORDS = [
            (285,360)
         ]

def main():
    while True:
        t1 = time.perf_counter()
        pixel = ImageGrab.grab().getpixel(COORDS[0])
        if sum(pixel)/3 < 170:
            keyboard.send('space')
        print(1/(time.perf_counter()-t1), end='\r')
        
main()