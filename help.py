import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def error_checking(command, size):
   try:
       command = command.replace(".", "")
       command = int(command)

   except ValueError:
       print("You must choose one of the number options!")
       return -1

   if (int(command) < 1) or (int(command) > size):
       print("You must choose one of the number options!")
       return -1

   return int(command)

def ls():
    delay_print(">help ls")
    print("The 'ls' command displays all the directories and files in the current directory")

def cd():
    delay_print(">help cd")
    print("The 'cd' command lets you choose a new directory to move to")
    print("Example: 'cd Pictures' changes to the Pictures directory")

def cat():
    delay_print(">help cat")
    print("The 'cat' command lets you print a file's contents to the screen")
    print("Example: 'cat mypasswords.txt' will print any text in the file to this screen")

def ssh():
    delay_print(">help ssh")
    print("The 'ssh' command allows you to switch to a different user on a network using the username and password")
    print("Example: 'ssh burd@192.168.0.2' will switch to burd on the 192.168.0.2 network")

def helphelp():
    delay_print(">help help")
    print("Seriously?... \nThe 'help' command gives information on how to use different commands")

def level1main():
    while True:
        print("What command do you need help with? \n1. ls \n2. cd \n3. cat \n4. ssh \n5. help \n6. Go back")
        input = error_checking(input(">"), 5)
        if input == -1:
            return
        if input == 1:
            ls()
        if input == 2:
            cd()
        if input == 3:
            cat()
        if input == 4:
            ssh()
        if input == 5:
            helphelp()
        if input == 6:
            return
def level2main():
    while True:
        delay_print("What should I do?")
        input = error_checking(input(">"), 5)
def level3main():
    while True:
        delay_print("What should I do?")
        input = error_checking(input(">"), 5)
def level4main():
    while True:
        delay_print("What should I do?")
        input = error_checking(input(">"), 5)

def help (level):
    if level == 1:
        level1main()
    if level == 2:
        level2main()
    if level == 3:
        level3main()
    if level == 4:
        level4main()