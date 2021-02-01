from PIL import ImageGrab
import time
import keyboard
import os
from copy import deepcopy



os.environ["DISPLAY"] = ":0"

end = 380
xs = list(range(250,end,1))
COORDS = [
            [x, 360] for x in xs
         ]
height_coords = (end, 340)

DINO = 260
print(COORDS)


def main():
    counter = 0
    queue = [0]
    beginig_flag = True
    height_flag = False
    while True:
        frame = ImageGrab.grab()
        pixels = [frame.getpixel(tuple(coord)) for coord in COORDS]
        height_pixel = frame.getpixel(height_coords)
        if (83,83,83) in pixels:
            if height_pixel == (83,83,83):
                height_flag = True
            time_pos = time.perf_counter()
            if beginig_flag:
                timestamp = time_pos
                beginig_flag = False
            else:
                timestamp = time_pos-queue[-1]
                #print(timestamp)
            if timestamp > 0.5:
                jump(height_flag)
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
        counter += 0
        if counter == 100:
            counter = 0
            xs.append(xs[-1]+2)
            COORDS.append([xs[-1], 360])
            print(COORDS)

def jump(flag):
    if flag:
        keyboard.press('space')
        time.sleep(0.5)
        keyboard.release('space')
    else:
        keyboard.send('space')



main()
