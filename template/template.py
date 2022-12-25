# This is sample template that have the required function calls (**) to run the bot

from pybot import PyBot

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

    # Resize the target window
    #bot.resize(640,380)

    # (**) Run the bot
    # (**) To modify the bot actions, modify the function __actions__ in BotHandler class
    bot.run()
    



# Driver code
if __name__ == '__main__':
    main()