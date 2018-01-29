import sys
import time

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def Main():
    cprint(figlet_format('Push the Button', font='starwars'),
            attrs=['bold'])

    time.sleep(3)

    input("Press ENTER to START")

if __name__=="__main__":
    Main()