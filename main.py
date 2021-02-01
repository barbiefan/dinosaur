from PIL import ImageGrab
import time
import keyboard
import os
import numpy

os.environ["DISPLAY"] = ":0"

y1 = 330 #y2-y1=15
y2 = 345
y3 = 346 #y4-y3=19
y4 = 365

x1 = 300+20 #x2-x1=50
x2 = 360+20

upper_flag = []
lower_flag = []

DINO = 260

def main():
    upper_flag = False
    lower_flag = False
    while True:
        time.sleep(0.05)

        frame = ImageGrab.grab()
        pixels = numpy.array(frame)
        upper_zone = pixels[y1:y2,x1:x2]
        lower_zone = pixels[y3:y4,x1:x2]

        if (83,83,83) in upper_zone:
            upper_flag = True
        if (83,83,83) in lower_zone:
            lower_flag = True
        action(upper_flag, lower_flag)
        upper_flag, lower_flag = False, False

def action(u_flag, l_flag):
    if u_flag:
        if l_flag:
            jump(True)
        else:
            duck(0.4)
    elif l_flag:
        jump(False)
        
def duck(sec):
    keyboard.press('down arrow')
    time.sleep(sec)
    keyboard.release('down arrow')

def jump(long):
    if not long:
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

'''
if up and low: jump long
if up but not low: duck
if not up but low: jump short
'''