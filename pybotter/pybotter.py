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
        self.bothandler.add_image(name, path)

    def find_image(self, name, threshold = 0.5):
        self.bothandler.find_image(name, threshold)

    def show_window(self):
        self.bothandler.show_screenshot()


    def run(self, debug = None):

        # Start program text
        print("""Hold shift + ESC to stop
        Hold shift + P to pause/unpause.
        Hold shift + F to show FPS
        Program is running.
        """)

        # Run the bot
        self.bothandler.run(debug)

        # After done running
        print('Program is closed.')
        i = input("Press any key to end program.\n")
        return 0


    def left_click(self, x, y, duration):
        self.bothandler.leftclick(x, y, duration)

    def resize(self, x, y):
        self.bothandler.resize(x, y)
        

    