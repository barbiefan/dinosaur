from PIL import ImageGrab
import time
import keyboard
import os
import numpy

os.environ["DISPLAY"] = ":0"

background = (32,33,36)
enemy = (172,172,172)

y1 = 413 #y2-y1=15
y2 = 437
y3 = 438 #y4-y3=19
y4 = 470

x1 = 131 #x2-x1=50
x2 = 220

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

        if enemy in upper_zone:
            upper_flag = True
        if enemy in lower_zone:
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