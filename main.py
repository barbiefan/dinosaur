from PIL import ImageGrab
import time
import keyboard
import os
from copy import deepcopy



os.environ["DISPLAY"] = ":0"

end = 340
xs = list(range(290,end,1))
COORDS = [
            [x, 360] for x in xs
         ]
height_coords = [
            (end, 340),
            (end-2, 340),
            (end-4, 340)
         ]
passed_coords = (200, 360)

DINO = 260
print(COORDS)


def main():
    counter = 0
    forward_queue = [0]
    height_flag = False
    while True:
        frame = ImageGrab.grab()
        pixels = [frame.getpixel(tuple(coord)) for coord in COORDS]
        height_pixels = [frame.getpixel(coord) for coord in height_coords]
        #passed_pixel = frame.getpixel(passed_coords)
        time_pos = time.perf_counter()
        if (83,83,83) in height_pixels:
            height_flag = True
        if (83,83,83) in pixels:
            timestamp = time_pos-forward_queue[-1]
            if timestamp > 0.5:
                jump(height_flag)
                forward_queue.pop(0)
                forward_queue.append(time_pos)
                print("jumped", forward_queue)
                height_flag = False
        #if passed_pixel == (83,83,83):
        #   print('ducked for 0.2')
        #    duck(0.2)


        #elif height_flag:
        #    duck()

        '''
        if sum(pixel1)/3 < 170:
            timestamp = time.perf_counter()-queue[-1]
            if timestamp > 0.5:
                print("pixel1", queue)
                velocity = DISTANCE/(time.perf_counter()-queue.pop(0))
                print(velocity)
        ''' 
        counter += 0
        if counter == 100:
            counter = 0
            xs.append(xs[-1]+2)
            COORDS.append([xs[-1], 360])
            print(COORDS)

def duck(sec):
    keyboard.press('down arrow')
    time.sleep(sec)
    keyboard.release('down arrow')

def jump(flag):
    if not flag:
        keyboard.press('space')
        time.sleep(0.2)
        keyboard.release('space')
        print('short jumped')
        duck(0.1)
        print('ducked')
    else:
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
        print('long jumped')

main()
