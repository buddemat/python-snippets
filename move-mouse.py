import pyautogui
import time

while True:
    pyautogui.moveTo(100,350)
    pyautogui.scroll(10)
    time.sleep(1)
    pyautogui.scroll(-10)
    pyautogui.moveTo(100,250)
    time.sleep(60)
