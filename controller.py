# The Observer watches for any file change and then dispatches the respective events to an event handler.
from tkinter.ttk import Style

from watchdog.observers import Observer
# The event handler will be notified when an event occurs.
from watchdog.events import FileSystemEventHandler
import time
import config
import os
from checker import FileChecker
import datetime
from colorama import Fore, init

init()

GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Fore.RESET
RED = Fore.RED
YELLOW = Fore.YELLOW

event2color = {
    "created": GREEN,
    "modified": BLUE,
    "deleted": RED,
    "moved": YELLOW,
}

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)