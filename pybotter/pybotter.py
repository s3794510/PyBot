from .bothandler import BotHandler
from .windowhandler import WindowHandler

class PyBot:
    
    def mainloop(self, func):
        def run():
            # Start program text
            print("""Hold shift + ESC to stop
            Hold shift + P to pause/unpause.
            Hold shift + F to show FPS
            Program is running.
            """)

            # Run the bot
            return_code = self.runmainloop(func)

            # After done running
            print('Program is closed.')
            return return_code
        return run

    def runmainloop(self, actions):
        while(self.bothandler.is_running):
    
            # get an updated image of the game
            self.bothandler.update_screenshot()

            # debug: pop up a window that show the screen shot
            #if(self.debug):
                #self.bothandler.show_screenshot()

            # Put the actions (mouse/keyboard) inside function actions in this class
            actions()

            self.bothandler.flow_handle()
        self.bothandler.destroyAllWindows()
        return 0

    def variables(self, func):
        def run(*args, **kwargs):
            self.bothandler.init(self.debug)
            return_code = func(*args, **kwargs)
            return return_code
        return run

    def __init__(self, window_name, debug = None):
        self.debug = debug
        self.window_name = window_name
        self.bothandler = BotHandler(window_name, self.debug)
        print("Object PyBot created, Window name: ", self.window_name)

    def list_windows():
        return WindowHandler.list_window_titles()

    def add_image(self, name, path):
        return self.bothandler.add_image(name, path)

    def find_image(self, name, threshold = 0.5, convert=None):
        "convert method = COLOR_BGR2GRAY"
        return self.bothandler.find_image(name, threshold,convert=convert)

    def show_window(self):
        self.bothandler.show_screenshot()


    def left_click(self, x, y, duration):
        self.bothandler.leftclick(x, y, duration)

    def key_press(self, key, duration):
        return self.bothandler.keyboard_press(key, duration)

    def resize(self, x, y):
        return self.bothandler.resize(x, y)
        