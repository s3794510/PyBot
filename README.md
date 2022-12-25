# Pybotter: Program Automation Python Library
Using Python
Currently under development

## Installation
Run the following command to install:

```python
pip install pybotter
```

## Usage

```python
from pybot import PyBot

# Define window name
window_name = "Title of the target window"

# Create PyBot object:
bot = PyBot(window_name)

# (**) To modify the bot actions, modify the function __actions__ in BotHandler class

# (**) Run the bot
bot.run()
```

Sound effects obtained from https://www.zapsplat.com
