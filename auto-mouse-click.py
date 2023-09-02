import time
import pyautogui

def click_mouse():
    while True:
        pyautogui.click()
        time.sleep(1)

if __name__ == "__main__":
    click_mouse()
