from PIL import ImageGrab
import time
import keyboard
import os
from copy import deepcopy



os.environ["DISPLAY"] = ":0"


xs = list(range(250,400,2))
print(xs)
COORDS = [
            (x, 360) for x in xs
         ]
DINO = 260


def main():
    queue = [0]
    flag = True
    while True:
        frame = ImageGrab.grab()
        pixels = [frame.getpixel(coord) for coord in COORDS]
        if (83,83,83) in pixels:
            time_pos = time.perf_counter()
            if flag:
                timestamp = time_pos
                flag = False
            else:
                timestamp = time_pos-queue[-1]
                #print(timestamp)
            if timestamp > 0.5:
                jump()
                queue.pop(0)
                queue.append(time_pos)
                print("jumped", queue)
        '''
        if sum(pixel1)/3 < 170:
            timestamp = time.perf_counter()-queue[-1]
            if timestamp > 0.5:
                print("pixel1", queue)
                velocity = DISTANCE/(time.perf_counter()-queue.pop(0))
                print(velocity)
        ''' 

def jump():
    keyboard.send('space')



main()
