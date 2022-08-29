import time

try:
    import pyautogui
    from pynput.mouse import Button, Controller
    from pynput.keyboard import Key
    from pynput.keyboard import Controller as KeyboardController
except ModuleNotFoundError:
    print("To run this demo, you need the python package: pynput")
    print("Can be installed with: pip install pynput")
    import sys
    sys.exit()

time.sleep(5)
pyautogui.press("left")

keyboard=KeyboardController()
keyboard.tap(Key.right)
keyboard.tap(Key.up)