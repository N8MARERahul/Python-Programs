import pyautogui
import time
time.sleep(2)
count = 1
while count <= 20:
    pyautogui.typewrite("bokachele")
    pyautogui.press("enter")
    count += 1