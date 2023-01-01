import time
import unittest
import sys, os, cv2
from pybotter import PyBot
from pybotter.vision import Vision
from tkinter import Tk, Button, Frame
from threading import Thread
import win32gui

class MockWindow(Tk):              
    def __init__(self):
        Tk.__init__(self)   
        singleButton = Button(self, text="Sample", padx=200, pady=50)
        singleButton.pack()

    def createWidgets(self):
        self.quitButton = Button(self, text='Quit',
            command=self.quit) # exits background (gui) thread
        self.quitButton.grid(row=1,column=0)    
        self.printButton = Button(self, text='Print',command=lambda: self.printHello())         
        self.printButton.grid(row=1,column=1) 

def runtk(window_title):  # runs in background thread
    app = MockWindow()                        
    app.title(window_title)     
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
        cls.window_title ="Test window pybotter for unit test"
        cls.thd = start_tkinter_thread(cls.window_title)
        check_window_created(cls.window_title)
        cls.needle_name = "SampleButton"
        cls.needle_path = "SampleButton.png"
        cls.interval = 0.2
        cls.step = 0.01
        cls.start_step = 0.3
        with disableConsolePrint():
            cls.pybotter = PyBot(cls.window_title)
        cls.pybotter.add_image(cls.needle_name, cls.needle_path)
        cls.pybotter.resize(640,480)

        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_series_image(self):
        current_step = self.start_step
        total_fail, total_success = 0,0
        max_step = None
        while current_step < 1:
            current_step += self.step
            start_time = time.time()
            if current_step > 1:
                current_step = 1
            while (start_time + self.interval > time.time()):
                self.pybotter.bothandler.update_screenshot()
                cor = self.pybotter.find_image(self.needle_name,current_step)
                if (cor.__len__() > 0):
                    msg = "Test successful at step: " + current_step.__str__() + " Test run time: " + (time.time() - start_time).__str__()
                    print(msg)
                    total_success += 1
                    max_step = current_step
                    break
            if msg == None:
                msg = "Test fail at step: " + current_step.__str__() + " Test run time: " + (time.time() - start_time).__str__()
                print (msg)
                total_fail += 1
            msg = None
        print("Total runs: ", total_fail + total_success)
        print("Fails: ", total_fail)
        print("Successes: ", total_success)
        print("Highest success step: ", max_step)
                        
                    


if __name__ == "__main__":
   #unittest.main(sys.argv[1:])
   unittest.main()