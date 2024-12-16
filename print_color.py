from Modules.colors_module import bcolors

def print_yellow(text):
    print(bcolors.WARNING + text + bcolors.ENDC)
def print_red(text):
    print(bcolors.FAIL + text + bcolors.ENDC)
def print_green(text):
    print(bcolors.OKGREEN + text + bcolors.ENDC)
def print_bold(text):
    print(bcolors.BOLD + text + bcolors.ENDC)
def print_underline(text):
    print(bcolors.UNDERLINE + text + bcolors.ENDC)
def print_cyan(text):
    print(bcolors.OKCYAN + text + bcolors.ENDC)
def print_okblue(text):
    print(bcolors.okblue + text + bcolors.ENDC)
def print_pink(text):
    print(bcolors.MAGENTA + text + bcolors.ENDC)
