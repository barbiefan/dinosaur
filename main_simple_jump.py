from PIL import ImageGrab
import time
import PIL
import keyboard
import os
import numpy

os.environ["DISPLAY"] = ":0"

background = [32,33,36]
enemy = (172,172,172)

DINO = 245
off = 360
buff = off

x1 = DINO+off
y1 = 600
x2 = DINO+off
y2 = 700


def main():
    upper_flag = False
    lower_flag = False
    while True:
        frame = ImageGrab.grab()
        nframe = numpy.array(frame)
        upper_zone = nframe[y1,x1-buff:x1]
        lower_zone = nframe[y2,x2-buff:x2]
        if enemy in upper_zone:
            upper_flag = True
        if enemy in lower_zone:
            lower_flag = True
        action(upper_flag, lower_flag)
        upper_flag, lower_flag = False, False

def action(u_flag, l_flag):
    if u_flag and not l_flag:
        duck()
    if l_flag:
        jump()
        
def duck():
    keyboard.press('down arrow')
    time.sleep(0.5)
    keyboard.release('down arrow')

def jump():
        keyboard.press('space')
        time.sleep(0.1)
        keyboard.release('space')

def save_detection_area_example():
    im = PIL.Image.open('sample.png')
    im = numpy.array(im)
    im[y1,x1-buff:x1] = (255,0,0)
    im[y2,x2-buff:x2] = (0,0,255)
    im_ = PIL.Image.fromarray(im)
    im_.save('area.png')

#save_detection_area_example()
time.sleep(2)
main()

'''
if up and low: jump long
if up but not low: duck
if not up but low: jump short
'''