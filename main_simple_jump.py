from PIL import ImageGrab
import time
import keyboard
import os
import numpy

os.environ["DISPLAY"] = ":0"

background = [32,33,36]
enemy = (172,172,172)

off = 60

x1 = 240+off
y1 = 405
x2 = 240+off
y2 = 460

DINO = 260

def main():
    upper_flag = False
    lower_flag = False
    while True:
        frame = ImageGrab.grab()
        nframe = numpy.array(frame)
        upper_zone = nframe[y1-10:y1+10,x1-10:x1+10]
        lower_zone = nframe[y2-10:y2+10,x2-10:x2+10]
        if enemy in upper_zone:
            upper_flag = True
        if enemy in lower_zone:
            lower_flag = True
        action(upper_flag, lower_flag)
        upper_flag, lower_flag = False, False

def action(u_flag, l_flag):
    if u_flag:
        print('duck')
        duck()
    if l_flag:
        print('jump')
        jump()
        
def duck():
    keyboard.press('down arrow')
    time.sleep(0.3)
    keyboard.release('down arrow')

def jump():
        keyboard.press('space')
        time.sleep(0.2)
        keyboard.release('space')

main()

'''
if up and low: jump long
if up but not low: duck
if not up but low: jump short
'''