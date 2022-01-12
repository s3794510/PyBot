from typing import Tuple
import  win32gui, win32api, win32con, sched, threading
from time import time, sleep
import keyboard, cv2, os
from .vision import Vision
from .windowhandler import WindowHandler
from pygame import mixer
class BotHandler:
    # http://www.kbdedit.com/manual/low_level_vk_list.html
    keymap = {
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
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
    'U': 0x57,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A 
    }
   
    
    def __init__(self, window_name, debug = None) -> None:
        self.window_name = window_name
        self.hwnd = None
        if self.window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, self.window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(self.window_name))
        self.s = sched.scheduler(time, sleep)
        self.window_handler = WindowHandler(self.window_name)
        self._active = True
        self._paused = False
        self.loop_time = time()
        self.fps = -1
        self.screenshot = None
        self.debug = debug
        self.images = {str:Vision}
        self.soundpath = os.path.join(os.path.dirname(__file__),os.pardir,os.pardir,'sound')
    
    def add_image(self, name, path):
        self.images.update({name:Vision(path)})
        print(f"{name} needle image added\n")

    def find_image(self, name, threshold):
        image = self.images.get(name)
        if image == None: 
            raise (f"Image {name} not registered")
        image.find(self.screenshot, threshold)

    def keyboard_press(self, key, duration):
        keycode = self.keymap.get(key.upper())
        win32api.PostMessage(self.hwnd, win32con.WM_KEYDOWN, keycode, 0)
        sleep(duration + 0.1)
        win32api.PostMessage(self.hwnd, win32con.WM_KEYUP, keycode, 0)

    def leftclick(self, x, y, duration):
        lParam = win32api.MAKELONG(x, y)
        win32gui.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        sleep(duration)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)


    def flow_handle(self, sleep_time = 0, debug = 'regular'):
        sleep(sleep_time)
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv2.waitKey(1) == ord('q'):
            self.exit()
        if (debug):
            # calcualte times processed each second
            self.fps = 1 / (time() - self.loop_time)
            self.loop_time = time()


    def init(self, debug = None):
        print("""Hold shift + ESC to stop
Hold shift + P to pause/unpause.
Hold shift + F to show FPS
Program is running.
        """)
        self.sound_start()
        # init threads
        self.pause_handle_thread()
        self.exit_handle_thread()
        self.show_fps_handle_thread()

        # initialize the Vision class
        #self.area_img = Vision('areasxx.jpg')
        #self.teleport_img = Vision('teleport.jpg')

    def resize(self, x, y):
        self.window_handler.window_resize(x, y)

    def run(self, actions, *args, **kwargs):
        self.init()
        # program loop
        while(self._active):
            # get an updated image of the game
            self.update_screenshot()
            #debug
            if(self.debug):
                self.show_screenshot()
            actions(*args, **kwargs)
            self.flow_handle(0)
        cv2.destroyAllWindows()
        print('Program is closed.')
        i = input("Press any key to end program.\n")
    def pause(self):
        self._paused = True
        print("Paused.\n")
        self.sound_pause()

    def unpause(self):
        self._paused = False
        print("Continued.\n")
        self.sound_unpause()
        pass
    def exit(self):
        self._active = False
        self.sound_exit()
        pass

    def sound_pause(self):
        self.play(self.soundpath +'/pause.mp3')

    def sound_unpause(self):
        self.play(self.soundpath +'/unpause.mp3')

    def sound_start(self):
        self.play(self.soundpath +'/start.mp3')

    def sound_exit(self):
        self.play(self.soundpath +'/exit.mp3')

    def play(self, sound_file):
            thread = threading.Thread(target=self.launch_mp3, args=(sound_file,))
            thread.start()

    def launch_mp3(self, sound_file):
            mixer.init()
            mixer.music.load(sound_file)
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                sleep(1)
    
    def pause_handle_thread(self):
        thread = threading.Thread(target=self.pause_handle, args=())
        thread.start()


    def pause_handle(self, sleep_time = 0.05):
        done = True
        while self._active:
            sleep(sleep_time)
            if done:
                if not self._paused and keyboard.is_pressed('p') and keyboard.is_pressed('shift'):
                    done = False
                    self.pause()
                    sleep(0.5)
                    done = True
                    
            if done:
                if self._paused and keyboard.is_pressed('p') and keyboard.is_pressed('shift'):   
                    done = False   
                    self.unpause()
                    sleep(0.5)
                    done = True
                    
                

    def exit_handle_thread(self):
        thread = threading.Thread(target=self.exit_handle, args= ())
        thread.start()
    
    def exit_handle(self, sleep_time = 0.05):
        while self._active:
            sleep(sleep_time)
            if keyboard.is_pressed('esc') and keyboard.is_pressed('shift'):
                self.exit()


    def show_fps_handle_thread(self):
        thread = threading.Thread(target=self.show_fps_handle, args= ()) 
        thread.start()

    def show_fps_handle(self, sleep_time = 0.1):
        while self._active:
            sleep(sleep_time)
            if keyboard.is_pressed('f') and keyboard.is_pressed('shift'):
                print(f"FPS: {self.fps}")
                print("Threads: ", threading.active_count())
                sleep(1)

    def update_screenshot(self, debug = None):
        self.screenshot = self.window_handler.get_screenshot(debug)

    def show_screenshot(self):
        cv2.imshow("Screenshot", self.screenshot)

    def actions(self):
        # bot actions
        points = self.area_img.find(self.screenshot, 0.8, self.debug, cv2.COLOR_BGR2GRAY)
        if not (len(points)):
            self.keyboard_press('v', 0)
            pass
        if (len(points)):
            points = self.teleport_img.find(self.screenshot, 0.95, self.debug, cv2.COLOR_BGR2GRAY)
            if (len(points)):
                x,y = points[0]
                self.leftclick(x,y, 0)
        

class PropagatingThread(threading.Thread):
    def run(self):
        self.exc = None
        try:
            if hasattr(self, '_Thread__target'):
                # Thread uses name mangling prior to Python 3.
                self.ret = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            else:
                self.ret = self._target(*self._args, **self._kwargs)
        except BaseException as e:
            self.exc = e

    def join(self, timeout=None):
        super(PropagatingThread, self).join(timeout)
        if self.exc:
            raise self.exc
        return self.ret
'490, 294'
'621, 405'

'131, 116'