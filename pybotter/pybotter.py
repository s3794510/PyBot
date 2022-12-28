from .bothandler import BotHandler
from .windowhandler import WindowHandler

class PyBot:
    def __init__(self, window_name, debug = None):
        self.debug = debug
        self.window_name = window_name
        self.bothandler = BotHandler(window_name, self.debug)
        print("Object PyBot created")

    def list_windows():
        return WindowHandler.list_window_titles()

    def add_image(self, name, path):
        return self.bothandler.add_image(name, path)

    def find_image(self, name, threshold = 0.5):
        return self.bothandler.find_image(name, threshold)

    def show_window(self):
        self.bothandler.show_screenshot()


    def run(self):

        # Start program text
        print("""Hold shift + ESC to stop
        Hold shift + P to pause/unpause.
        Hold shift + F to show FPS
        Program is running.
        """)

        # Run the bot
        self.mainloop()

        # After done running
        print('Program is closed.')
        return 0

    def mainloop(self):
        self.bothandler.init(self.debug)
        self.add_image("Sample button", "SampleButton.png")
        while(self.bothandler.is_running):
    
            # get an updated image of the game
            self.bothandler.update_screenshot()

            # debug: pop up a window that show the screen shot
            #if(self.debug):
                #self.bothandler.show_screenshot()

            # Put the actions (mouse/keyboard) inside function actions in this class
            self.actions()

            self.bothandler.flow_handle()
        self.bothandler.destroyAllWindows()


    def left_click(self, x, y, duration):
        self.bothandler.leftclick(x, y, duration)

    def key_press(self, key, duration):
        return self.bothandler.keyboard_press(key, duration)

    def resize(self, x, y):
        return self.bothandler.resize(x, y)
        

    def actions(self):
        # Put the actions here
        self.find_image("Sample button",0.5)
        pass