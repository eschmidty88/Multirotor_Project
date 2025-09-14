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
dino_location = pyautogui.locateOnScreen('dino.png') 
print(dino_location)

# Move the mouse to the center of the dinosaur
pyautogui.center(dino_location)
reference_color = getpixelcolor.average(760, 420, 10, 10)

# Mpve the mouse to center of scanning region
pyautogui.moveTo(745, 431)

# Start game
pyautogui.press('up')
# pyautogui.mouseInfo()


# Loop 948, 394
while True:
    current_color = getpixelcolor.average(745, 424, 10, 10)
    if not np.array_equal(current_color, reference_color):
        # pyautogui.press('up')
        pyautogui.keyDown('up')
        time.sleep(0.04)
        pyautogui.keyUp('up')
        time.sleep(0.002)
        pyautogui.keyDown('down')
        time.sleep(0.08)
        pyautogui.keyUp('down')
        #time.sleep(0.02)
    
    restart_color = getpixelcolor.average(948, 384, 10, 10)
    if not np.array_equal(restart_color, reference_color):
        pyautogui.press('up')
