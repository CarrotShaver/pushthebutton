# Level 4

import  sys
import time
import os

def main():
	print("""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#&@@@@@@@@&%#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@&&&&&&*@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@/%@@@@@@@@(/*,,,**/#%&&&&&&&&((@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@%/@@@@@@@(,,,,,,,,,,,,,,,,,,,(%&&&&&%.@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@/%@@@@@&/,,,,,,,,,,,,,,,,,,,,,,,,,*#&%%%%(%@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@%#@@@@@%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(%%%%%*@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@*@@@@@#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/%%%%%.@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(%%%%/@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*%%%%/@@@@@@@@@@@@@
	@@@@@@@@@@@@&@@@@*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*####(@@@@@@@@@@@@
	@@@@@@@@@@@/@@@@*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*####*@@@@@@@@@@@
	@@@@@@@@@@(@@@@(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*####&@@@@@@@@@@
	@@@@@@@@@@#@@@&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,(###*@@@@@@@@@@
	@@@@@@@@@@%@@@(,&@@@@@@@@@,,%@#,,,,,%@(,%@@@@@@@@(,*@@,,,,,,&@#,*###/@@@@@@@@@@
	@@@@@@@@@@&@@@*,&@&,,,,,&@(,%@#,,,,,%@(,@@%((///*,,*@@@@@@@@@@#,*#(((@@@@@@@@@@
	@@@@@@@@@@&@@@*,&@@@@@@@@#,,#@&,,,,,@@(,##,,,,,(@@,*@@,,,,,,&@#,*#((/&@@@@@@@@@
	@@@@@@@@@@%@@@(,%@&,,,,,,,,,,#&@@@@@@#,,/&@&@@@@&/,*@&,,,,,,&@#,*(((*&@@@@@@@@@
	@@@@@@@@@@/@@@&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,((((*&@@@@@@@@@
	@@@@@@@@@@/&&&&(,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*((((%&@@@@@@@@@
	@@@@@@@@@@@.&&&&/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*((((.&@@@@@@@@@@
	@@@@@@@@@@@@/&&&&/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*((((,%&@@@@@@@@@@
	@@@@@@@@@@@@%,&&&,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/(((( %&@@@@@@@@@@@
	@@@@@@@@@@@@@@.&&&&%/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*((((( %&@@@@@@@@@@@@
	@@@@@@@@@@@@@@@.(%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/((((*.%&@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@# %%%%%%*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*((((// %&@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@*.#%%%%%(*,,,,,,,,,,,,,,,,,,,,,,,*/(((((/ (&&@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@#./%%%%%%#/*,,,,,,,,,,,,,,,**(((((((, %&@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@/ /%#########(((((((((((((((((, #&@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@& .(########(((((((((((*..&@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(. .,*///*,  ,%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	""")
	DONE = input("PUSH THE BUTTON")

	FINAL = input("ARE YOU SURE?\nPUSH AGAIN TO CONFIRM")

	os.system('clear')

	from colorama import init
	init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
	from termcolor import cprint
	from pyfiglet import figlet_format

	cprint(figlet_format('missile alert!', font='starwars'),
		   'yellow', 'on_red', attrs=['bold'])

	time.sleep(3)

	count =5

	while count > 0:
		os.system('clear')
		cprint(figlet_format(str(count), font='starwars'),
			  'yellow', 'on_red', attrs=['bold'])

		count = int(count) - 1

		time.sleep(1)


	os.system('clear')
	os.system('clear')
	print(""" ...............................................................................
	...............................................................................
	...............................................................................
	....................................       ....................................
	...............................                 ...............................
	...................       ..                       ..       ...................
	................                                               ................
	..............                                                   ..............
	.............                                                     .............
	...........                                                         ...........
	.........                                                             .........
	.......                                                                 .......
	......                                                                   ......
	......                                                                   ......
	......                                                                   ......
	.......                                                                 .......
	........                                                               ........
	...........             .....        ....          .....            ...........
	...............................................................................
	...............................................................................
	.............................       .......       .............................
	.............................       .......       .............................
	....................        .       .......       .       .....................
	.................          ..       .......       ..          .................
	................                   .........                   ................
	.................                                             .................
	...................                                         ...................
	........................                               ........................
	...............................................................................
	.........................   .......................   .........................
	.......................        .................        .......................
	....................          ...................          ....................
	................             .....................             ................
	................                                               ................
	................                                               ................
	................                                               ................
	................                                               ................
	...............................................................................
	...............................................................................""")

	cprint(figlet_format('GAME OVER', font='starwars'),
		   'yellow', 'on_red', attrs=['bold'])
	
if __name__=="__main__":
	main()
