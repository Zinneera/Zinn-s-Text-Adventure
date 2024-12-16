import sys, time
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Modules.colors_module import bcolors

def type_print(text, delay=0.05, color=""):
    """
    Prints text with a typewriter effect, supporting optional color.
    Args:
        text (str): The text to print.
        delay (float): The delay between each character (in seconds).
        color (str): The ANSI color code for the text.
    """
    for char in text:
        sys.stdout.write(color + char + bcolors.ENDC)
        sys.stdout.flush()
        time.sleep(delay)
    print()