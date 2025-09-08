import pyautogui
import webbrowser
import time



browser = webbrowser.get()
browser.open('https://chromedino.com/')

time.sleep(3) 


for _ in range(1000):  
    pyautogui.press('up')
    time.sleep(0.1)  
