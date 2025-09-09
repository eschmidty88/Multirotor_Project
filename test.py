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
reference_color = getpixelcolor.average(770, 420, 10, 10)

# Mpve the mouse to center of scanning region
pyautogui.moveTo(770, 400)

# Start game
pyautogui.press('up')


# Loop
while True:
    current_color = getpixelcolor.average(770, 420, 10, 10)
    if not np.array_equal(current_color, reference_color):
        pyautogui.press('up')
        time.sleep(0.05)
