# This is sample template that have the required function calls (**) to properly invoke and run the bot

from pybotter import PyBot

def main():

    # Change path of the system
    #os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # (**) Type the exact name of the window
    window_name = "Title of the target window"

    # Show list of windows
    #PyBot.list_windows()

    # Debug mode: show screen shot of the target window
    debug = None
    #debug = 'debug' 
    
    # (**) Initialise the bot
    bot = PyBot(window_name, debug)

    # (**) Add needle images first
    @bot.variables
    def add_variables():
        #bot.add_image("IMAGE_NAME", "IMAGE_PATH")
        pass
    
    
    # (**) Add bot actions that run during the main loop
    @bot.mainloop
    def bot_run():
        pass


    # Resize the target window
    #bot.resize(640,380)

    # (**) Initiate adding variables, MUST RUN THIS BEFORE THE MAIN LOOP
    add_variables()
    
    # (**) Run the bot
    bot_run()
    
# Driver code
if __name__ == '__main__':
    main()