import pyautogui
import keyboard
import random, time,winsound
import win32api, win32con
import threading, multiprocessing
from time import sleep
class bot():
	pass


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def play(sound_file):
    thread = multiprocessing.Process(target=winsound.PlaySound, args=(sound_file, winsound.SND_ALIAS))
    thread.start()
    sleep(0.2)
while (True):
    if keyboard.is_pressed('alt'):
        
        play("sound/exit.wav")
    if keyboard.is_pressed('ctrl'):
        play("sound/start.wav")
