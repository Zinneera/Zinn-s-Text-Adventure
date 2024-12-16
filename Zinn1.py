###Started 12/14/24###

###Modules###
from Modules.typeprint_module import type_print, time
from Modules.direct_low import get_direction
from Modules.colors_module import bcolors
from Modules.print_color import print_yellow, print_red, print_green, print_bold, print_underline, print_cyan, print_okblue, print_pink
from Modules.word_colors import print_colored_sentence
###Comments###
###
def startscreen():
    type_print("New Game", delay=0.05, color=bcolors.WARNING)
    type_print("Exit")
    direction = get_direction()
    if direction == "new game":
        mainmenu()
    elif direction == "exit":
        print_yellow("Are you sure you want to exit? Y/N")
        direction = get_direction()
        if direction == "y":
            print_pink("You exit the curious void...")
            quit()
        elif direction == "n":
            startscreen()
        else:
            print("Please enter a valid input")
            startscreen()
    else:
        print("Please enter a valid input")
        startscreen()
def mainmenu():
    print_cyan("The heavy red-metal doors of the terminal slide open, overwhelming you with a flash of light.")
    time.sleep(1)
    print_yellow("'Attention, arrivals-'")
    time.sleep(1)
    print_cyan("A soothing, but quite enormously loud voice chimes over a nearby PA System.")
    time.sleep(1)
    print_yellow("'-please make your way to inbound-communications at terminal entry four for processing. Thank you.'")
    time.sleep(1)
    print_green("Type 'Go Back' to return to the Start Menu")
    direction = get_direction()
    if direction == "go back":
        startscreen()
    else:
        print("Please enter a valid input")
        mainmenu()
startscreen()