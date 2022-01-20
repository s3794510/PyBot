from typing import List, Tuple
from cv2 import resize, threshold
from .src.bothandler import BotHandler

class PyBot:
    def __init__(self, window_name, debug = None, **kwargs) -> None:
        self.__debug = debug
        self.__window_name = window_name
        self.__bothandler = BotHandler(self.__window_name, self.__debug)
        print("PYBOT: Object PyBot created\n")

    def add_image(self, name, path):
        self.__bothandler.add_image(name, path)

    def find_image(self, name, threshold = 0.5, convert = None, debug_mode = '') -> List:
        """convert methods = [None, cv2.COLOR_BGR2GRAY] \n
        debug_mode = [None, 'points', 'rectangles', 'show', 'save']"""
        return self.__bothandler.find_image(name, threshold, convert, debug_mode)

    def show_window(self):
        self.__bothandler.show_screenshot()


    def run(self, begin_wait, loop_wait, actions, *args, **kwargs):
        """begin_wait: time wait before start\n
        loop_wait: time wait before each loop\n
        actions: the loop will rung this function once\n
        """
        self.__bothandler.run(begin_wait, loop_wait, actions, *args, **kwargs)


    def left_click(self, location:Tuple, duration_sec):
        self.__bothandler.leftclick(location, duration_sec)

    def resize(self, x, y):
        self.__bothandler.resize(x, y)
        
    def key_press (self, key, duration_sec):
        self.__bothandler.keyboard_press(key, duration_sec)

    