import time
import unittest
import sys, os
from pybotter import PyBot
from tkinter import Tk, Button, Frame
from threading import Thread
import win32gui
from contextlib import contextmanager

class Application(Frame):              
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text='Quit',
            command=self.quit) # exits background (gui) thread
        self.quitButton.grid(row=1,column=0)    
        self.printButton = Button(self, text='Print',command=lambda: self.printHello())         
        self.printButton.grid(row=1,column=1) 

def runtk(window_title):  # runs in background thread
    app = Application()                        
    app.master.title(window_title)     
    app.mainloop()

def start_tkinter_thread(window_title):
    thd = Thread(target=runtk, args= (window_title,))   # gui thread
    thd.daemon = True  # background thread will exit if main thread exits
    thd.start()  # start tk loop
    return thd

def find_window(name):
    whnd = win32gui.FindWindowEx(None, None, None, name)
    if not (whnd == 0):
        return True

def check_window_created(window_title):
    start_time = time.time()
    while not find_window(window_title):
        if time.time() > start_time + 5:
            raise Exception("Mock window was not properly created.") 




class disableConsolePrint():
    def __enter__(self):
        sys.stdout = open(os.devnull, 'w',encoding="utf-8")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        
class TestPybotter(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.window_title ="Test window pybotter fro unit test"
        cls.thd = start_tkinter_thread(cls.window_title)
        check_window_created(cls.window_title)
        cls.pybotter = PyBot(cls.window_title)
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_targetwindow(self):
        with disableConsolePrint():
            self.assertEqual(self.pybotter.window_name, self.window_title)

    def test_add_image_fail(self):
        with disableConsolePrint():
            self.assertRaises(Exception, self.pybotter.add_image,"SampleButton", "SampleButon.png")

    def test_add_image(self):
        self.assertEqual(self.pybotter.add_image("SampleButton", "SampleButton.png"),0)
if __name__ == '__main__':
    unittest.main()

