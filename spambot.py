import time
import pyautogui

class FirstOfAll:
    def spam_bot(self=""):
        spam_text = input("text to spam: ")
        spam_times = input("Times to spam: ")
        int_spam_times = int(spam_times)
        print("starts spaming in: 3 seconds")
        time.sleep(1)
        print("starts spaming in: 2 seconds")
        time.sleep(1)
        print("starts spaming in: 1 seconds")
        time.sleep(1)
        for i in range(int_spam_times):
            pyautogui.typewrite(spam_text)
            pyautogui.press("enter")
instanz = FirstOfAll
instanz.spam_bot()
