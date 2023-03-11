from keyboard import press_and_release
from time import sleep
import pyautogui, pyperclip

def paste(text: str):    
    pyperclip.copy(text)
    press_and_release('ctrl + v')

def type(text: str, interval=0.0):    
    buffer = pyperclip.paste()
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            sleep(interval)
    pyperclip.copy(buffer)

type('Hello World!', 0.1)# Example