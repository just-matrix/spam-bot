import pyautogui
import time
print("options: '50' '100' '200' '300' '400' '500' '1000' 'unlimited'")
print("")
var = input("Times to spam the text : ")
word_spam = input("Text to spam : ")
print("[                     ] 0% ")
time.sleep(1)
print("[██████               ] 25%")
time.sleep(1)
print("[██████████           ] 50%")
time.sleep(1)
print("[████████████████     ] 75%")
time.sleep(1)
print("[█████████████████████] 100%")

if var == '50':
    f = open("50", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)

if var == '100':
    f = open("100", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)

if var == '200':
    f = open("200", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)

if var == '300':
    f = open("300", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)

if var == '400':
    f = open("400", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)

if var == '500':
    f = open("500", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)


if var == '1000':
    f = open("1000", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)

if var == 'unlimited':
    f = open("unlimited", "r")
    for w in f:
        pyautogui.typewrite(word_spam)
        pyautogui.press("enter")
        print("Text : ", word_spam)
