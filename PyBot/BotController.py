import sched
from time import sleep, time
from PIL.Image import init
import win32gui, win32ui, win32con, win32api, keyboard, winsound, pyautogui


class BotController:
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

    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        # bring each window to the front
        # win32gui.SetForegroundWindow(self.hwnd)
        self.s = sched.scheduler(time, sleep)
    
        
    # send a keyboard input to the given window
    def press_key(self, key, start_sec, hold_sec, foreground = False):
        priority = 2
        duration = start_sec + hold_sec
        keycode = self.keymap.get(key)
        if foreground:
            foreground_time = 0.15
            self.s.enter(start_sec - foreground_time, priority, win32gui.SetForegroundWindow, 
                    argument=(self.hwnd,))
        self.s.enter(start_sec, priority, win32api.SendMessage, 
                argument=(self.hwnd, win32con.WM_KEYDOWN, keycode , 0)) 
        self.s.enter(duration, priority, win32api.SendMessage, 
                argument=(self.hwnd, win32con.WM_KEYUP, keycode, 0))

        # win32gui.SetForegroundWindow(hwnd)
        # win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
        # sleep(sec)
        # win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)
        self.s.run()


    def click(self, x, y, start_sec, hold_sec):
        priority = 2
        duration = start_sec + hold_sec
        lParam = win32api.MAKELONG(x, y)
        self.s.enter(start_sec, priority, win32api.SendMessage, 
                argument=(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam))
        self.s.enter(duration, priority, win32api.SendMessage, 
                argument=(self.hwnd, win32con.WM_LBUTTONUP, None, lParam))
        self.s.run()
        
        #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)

        #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
        win32gui.EnumWindows(winEnumHandler, None)


    def get_inner_windows(self, whndl):
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
            return True
        hwnds = {}
        win32gui.EnumChildWindows(whndl, callback, hwnds)
        return hwnds


    def find_all_windows(self, name):
        result = []
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
                result.append(hwnd)
        win32gui.EnumWindows(winEnumHandler, None)
        return result




    def run(self):
        winsound.Beep(5000, 200)
        
        

    def exit(self):
        winsound.Beep(7000, 200)


    def debug(self, key):
        print(self.keymap.get(key))