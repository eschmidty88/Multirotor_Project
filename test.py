import pyautogui
import webbrowser
import time
import getpixelcolor
import numpy as np


# Open the Chrome Dino game in the web browser
browser = webbrowser.get()
browser.open('https://chromedino.com/')

time.sleep(3) 

# Locate the dinosaur on the screen
#dino_location = pyautogui.locateOnScreen('dino.png') 
#print(dino_location)

# Move the mouse to the center of the dinosaur
#pyautogui.center(dino_location)
reference_color = getpixelcolor.pixel(185, 347)
# Move the mouse to center of scanning region
x = 730
#770

y = 430
width = 30 
height = 10
#0.017
jump_length = 0.016
downtime = 0.06

pyautogui.moveTo(x, y)


# Start game
pyautogui.press('up')


# Loop 948, 394

while True:
    current_color = getpixelcolor.average(x, y, width , height)
    if not np.array_equal(current_color, reference_color):
    

        # pyautogui.press('up')
        pyautogui.keyDown('up')
        time.sleep(jump_length)
        pyautogui.keyUp('up')
        #time.sleep(downtime)
        pyautogui.keyDown('down')
        time.sleep(downtime)
        pyautogui.keyUp('down')


    restart_color = getpixelcolor.average(948, 384, 10, 15)
    if not np.array_equal(restart_color, reference_color):
        pyautogui.press('up')
        time.sleep(0.5)


