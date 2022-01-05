import win32gui
class BotHandler:
    hwnd = None
    def __init__(self, window_name) -> None:
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
            if not self.hwnd:
                raise Exception('Window not found: {}'.format(window_name))
        self.WindowHandler = self.WindowHandler(self.hwnd)
    

    class WindowHandler:
        def __init__(self, hwnd) -> None:
            self.hwnd = hwnd
        def window_resize(self, w, h) -> None:
            win32gui.MoveWindow(self.hwnd, 0, 0, w, h, True)
            
            
