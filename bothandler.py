from typing import Tuple
import win32gui
import win32api, win32con
import sched
from time import sleep, time
import keyboard, cv2

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
    def __init__(self, window_name) -> None:
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
        self.s = sched.scheduler(time, sleep)
        self.WindowHandler = self.WindowHandler(self.hwnd)
        self.is_running = True
        self.is_pause = False
    
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

    def flow_handle(self, sleep_time = 0, loop_time = None, debug = None):
        while True:
            sleep(sleep_time)
            if keyboard.is_pressed('esc') and keyboard.is_pressed('shift'):
                self.is_running = False
                return
            if not self.is_pause and keyboard.is_pressed('p') and keyboard.is_pressed('shift'):
                print("Paused.")
                self.is_pause = True
            elif keyboard.is_pressed('p') and keyboard.is_pressed('shift'):
                print("Continue")
                self.is_pause = False
            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            if cv2.waitKey(1) == ord('q'):
                self.is_running = False
                break
            if (debug):
                # debug the loop rate
                if keyboard.is_pressed('f') and keyboard.is_pressed('shift'):
                    print('FPS {}'.format(1 / (time() - loop_time)))
                    sleep(1)
                loop_time = time()
            if (self.is_pause == False):
                break
        if self.is_running == False:
            cv2.destroyAllWindows()
        return loop_time
'490, 294'
'621, 405'

'131, 116'