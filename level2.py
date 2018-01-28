import time
import help

def email():
    print("Hello everyone just letting you know, the port for SSH has been changed")
    print("unfortunately our tech guy forgot to write it down and has the memory of a goldfish")
    print("If only there was a way to find out the new port with a tool...")

def ls():
    print("1. Documents")
    print("2. Music")
    print("3. Emails")
    print("ls into ...")
    userinput2 = int(input())
    print('type', type(userinput2))
    if userinput2 == 1:
        print("essay.docx")
        print("timesheet.doc")
        print("slackingoff.doc")

    if userinput2 == 2:
        print("Michael Jackson - Billie Jean.mp3")
        print("Prince - Kiss.mp3")
        print("Will Smith - Fresh Prince of Bel Air.mp3")

    if userinput2 == 3:
        print("1. RE: LOGS")
        print("2. RE: TIMESHEET ADJUSTMENTS")
        print("3. RE: PORT CHANGES")
        print("What should you cat into..?")
        cat = int(input())
        if cat == 1:
            return
        if cat == 2:
            return
        if cat == 3:
            email()

    stall_tactic = input("press enter to continue")

def ssh():
    print("hello")
    return

def nmap():
    while True:
        print("Use nmap to scan available ports? (y/n)")
        userinput = input()
        if userinput == "y":
            print("scanning available ports...")
            print(".")
            print(".")
            print("nmap has found these available ports open:")
            print("Port: 53017")
            print("Port: 3878")
            print("Port: 8789")
            stall_tactic = input("press enter to continue")
            return
        if userinput == "n":
            return






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

def MainMenu():
    user = "Robin"
    while True:
        print("What Should I Do?")
        print("1. ls")
        print("2. cd")
        print("3. cat")
        print("4. nmap")
        print("5. ssh")
        print("6. help")
        userinput = input()
        userinput = error_checking(userinput, 6)
        if userinput == 1:
            ls()
        if userinput == 2:
            cd()
        if userinput == 3:
            cat()
        if userinput == 4:
            nmap()
        if userinput == 5:
            ssh()
        if userinput == 6:
            help.help(2)

def Main():
    print("You are logged in as Deborah the supervisor for the data entry team...")
    MainMenu()


if __name__ == '__main__':
    Main()