import pyautogui
import time
print("options for spam: '100'  '200'  '300' '400' '500' '1000'  'unlimited' ")
print("")
var = input("How many times to spam the text? : ")
text = input("text to spam : ")
print("")
print("it will start in 3 seconds")
time.sleep(3)
if var == '100':
    f = open("100", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
if var == '200':
    f = open("200", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
if var == '300':
    f = open("300", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
if var == '400':
    f = open("400", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
if var == '500':
    f = open("500", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
if var == '1000':
    f = open("1000", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
if var == 'unlimited':
    f = open("unlimited", "r")
    for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
