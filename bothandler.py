from typing import Tuple
import winsound
import win32gui, win32api, win32con
import sched, threading
from time import time, sleep
import keyboard, cv2
from vision import Vision
from windowcapture import WindowCapture

class BotHandler:
    # http://www.kbdedit.com/manual/low_level_vk_list.html
    VK_KEY_U =	0x55
    VK_KEY_V =	0x56
    VK_KEY_3 = 0x33
    keymap = {
    '0':	0x30,
    '1':	0x31,
    '2':	0x32,
    '3': 0x33,
    '''
    VK_KEY_4	0x34 ('4')	4
    VK_KEY_5	0x35 ('5')	5
    VK_KEY_6	0x36 ('6')	6
    VK_KEY_7	0x37 ('7')	7
    VK_KEY_8	0x38 ('8')	8
    VK_KEY_9	0x39 ('9')	9
    VK_KEY_A	0x41 ('A')	A
    VK_KEY_B	0x42 ('B')	B
    VK_KEY_C	0x43 ('C')	C
    VK_KEY_D	0x44 ('D')	D
    VK_KEY_E	0x45 ('E')	E
    VK_KEY_F	0x46 ('F')	F
    VK_KEY_G	0x47 ('G')	G
    VK_KEY_H	0x48 ('H')	H
    VK_KEY_I	0x49 ('I')	I
    VK_KEY_J	0x4A ('J')	J
    VK_KEY_K	0x4B ('K')	K
    VK_KEY_L	0x4C ('L')	L
    VK_KEY_M	0x4D ('M')	M
    VK_KEY_N	0x4E ('N')	N
    VK_KEY_O	0x4F ('O')	O
    VK_KEY_P	0x50 ('P')	P
    VK_KEY_Q	0x51 ('Q')	Q
    VK_KEY_R	0x52 ('R')	R
    VK_KEY_S	0x53 ('S')	S
    VK_KEY_T	0x54 ('T')	T
    VK_KEY_U	0x55 ('U')	U
    ''':0,
    'U':	0x57,
    'V':	0x56,
    'W':	0x57,
    'X':    0x58,
    'Y':    0x59,
    'Z':    0x5A 
    }
   
    hwnd = None
    def __init__(self, window_name, debug = None) -> None:
        self.window_name = window_name
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, self.window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(self.window_name))
        
        self.s = sched.scheduler(time, sleep)
        self.WindowHandler = self.WindowHandler(self.hwnd)
        self.is_running = True
        self.is_pause = False
        self.loop_time = time()
        self.fps = -1

    def keyboard_press(self, key, duration):
        keycode = self.keymap.get(key.upper())
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, keycode, 0)
        sleep(duration + 0.1)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, keycode, 0)

    def leftclick(self, x, y, duration):
        lParam = win32api.MAKELONG(x, y)
        win32gui.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)

    class WindowHandler:
        def __init__(self, hwnd) -> None:
            self.hwnd = hwnd
        def window_resize(self, w, h) -> None:
            win32gui.MoveWindow(self.hwnd, 0, 0, w, h, True)
        def get_windowsize(self) -> Tuple:
            return win32gui.GetWindowRect(self.hwnd)

    def flow_handle(self, sleep_time = 0, debug = 'regular'):
        sleep(sleep_time)
        if (debug):
            # calcualte times processed each second
            self.fps = 1 / (time() - self.loop_time)
            self.loop_time = time()


    def init(self, debug = None):
        self.sound_start()
        # init threads
        self.pause_handle_thread()
        self.exit_handle_thread()
        self.show_fps_handle_thread()

        # resize window
        self.WindowHandler.window_resize(640, 360)

        # initialize the WindowCapture class
        self.wincap = WindowCapture(self.window_name)
        # initialize the Vision class
        self.area_img = Vision('areasxx.jpg')
        self.teleport_img = Vision('teleport.jpg')


    def run(self, debug = None):
        self.init()
        while(self.is_running):
            # get an updated image of the game
            screenshot = self.wincap.get_screenshot()
            # bot actions
            points = self.area_img.find(screenshot, 0.8, debug, cv2.COLOR_BGR2GRAY)
            if not (len(points)):
                self.keyboard_press('v', 0)
                pass
            if (len(points)):
                points = self.teleport_img.find(screenshot, 0.95, debug, cv2.COLOR_BGR2GRAY)
                if (len(points)):
                    x,y = points[0]
                    self.leftclick(x,y, 0)
            self.flow_handle(0)

    def pause(self):
        self.is_pause = True
        print("Paused.\n")
        self.sound_pause()

    def unpause(self):
        self.is_pause = False
        print("Continued.\n")
        self.sound_unpause()
        pass
    def exit(self):
        self.is_running = False
        self.sound_exit()
        cv2.destroyAllWindows()
        pass

    def sound_pause(self):
        self.play('sound/pause.wav')

    def sound_unpause(self):
        self.play('sound/unpause.wav')

    def sound_start(self):
        self.play('sound/start.wav')

    def sound_exit(self):
        self.play('sound/exit.wav')

    def play(self, sound_file):
        thread = threading.Thread(target=winsound.PlaySound, args=(sound_file, winsound.SND_ALIAS))
        thread.start()
    
    def pause_handle_thread(self):
        thread = threading.Thread(target=self.pause_handle, args=())
        thread.start()

    def pause_handle(self, sleep_time = 0.1):
        while self.is_running:
            sleep(sleep_time)
            if threading.active_count() < 7:
                if not self.is_pause and keyboard.is_pressed('p') and keyboard.is_pressed('shift'):
                    self.pause()
            if threading.active_count() < 7:
                if self.is_pause and keyboard.is_pressed('p') and keyboard.is_pressed('shift'):
                    self.unpause()
                

    def exit_handle_thread(self):
        thread = threading.Thread(target=self.exit_handle, args= ())
        thread.start()
    
    def exit_handle(self, sleep_time = 0.1):
        while self.is_running:
            sleep(sleep_time)
            if keyboard.is_pressed('esc') and keyboard.is_pressed('shift'):
                self.exit()
            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            if cv2.waitKey(1) == ord('q'):
                self.exit()

    def show_fps_handle_thread(self):
        thread = threading.Thread(target=self.show_fps_handle, args= ()) 
        thread.start()

    def show_fps_handle(self, sleep_time = 0.1):
        while self.is_running:
            sleep(sleep_time)
            if keyboard.is_pressed('f') and keyboard.is_pressed('shift'):
                print(f"FPS: {self.fps}")
                print("Threads: ", threading.active_count())
                sleep(1)

'490, 294'
'621, 405'

'131, 116'