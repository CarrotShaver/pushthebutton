import help

sshTrigger = False

def email( choice ):
    if choice == 1:
        print("Subject: Logs")
        print("Hello Supervisors, \nIt has come to our attention that many of you have been neglecting to do your end-of-day log reviews.")
        print("Please remember that reviewing logs is not only necessary, it is also part of your job.")
        print("Though it may seem tedious at first, many of our older staff can finish in less than three hours!")
        print("We're certain that if you keep up with your log reviews, not only will you keep your job, you'll feel a sense of pride and accomplishment.")
        print("Thanks,\nManagement")
    if choice == 2:
        print("Subject: Timesheet Adjustments")
        print("Hello Supervisors,\nAs you know, there has been a temporary government shutdown.  As such, we feel it is our duty and pleasure to inform you")
        print("that you will no longer be required to submit timesheets until further notice! While this means you will not be receiving pay,")
        print("we know that just being allowed to work here will give you a sense of pride and accomplishment.")
        print("Thanks,\nManagement")
    if choice == 3:
        print("Subject: Important! SSH Port Change")
        print("Hello Supervisors, \nAs you know, we've had to change the SSH port for our monitoring account due to security reasons.")
        print("Unfortunately, the IT technician forgot to include the new port in the e-mail and is currently unreachable.")
        print("He did say there was a tool to find it if we ever forgot, but didn't specify how.")
        print("If any of you can figure out, please let us know, as we're sure you'll feel a sense of pride and accomplishment.")
        print("If not, we will make sure to send out another e-mail when he returns after the weekend.")
        print("Thanks,\nManagement")

def ls():
    print("1. Documents")
    print("2. Music")
    print("3. Emails")
    print("4. Go back")
    print("cd into ...")
    userinput2 = error_checking(input(">"), 4)
    if userinput2 == 1:
        print("essay.docx")
        print("timesheet.doc")
        print("slackingoff.doc")

    if userinput2 == 2:
        print("Michael Jackson - Billie Jean.mp3")
        print("Prince - Kiss.mp3")
        print("Will Smith - Fresh Prince of Bel Air.mp3")

    if userinput2 == 3:
        print("1. RE: Logs")
        print("2. RE: Timesheet Adjustments")
        print("3. RE: Important! SSH Port Change")
        print("4. Exit Emails")
        print("cat what file?")
        cat = error_checking(input(">"), 4)
        if cat == 1:
            email(1)
        if cat == 2:
            email(2)
        if cat == 3:
            email(3)
        if cat == 4:
            return
    if userinput2 == 4:
        return

    input("press enter to continue")

def ssh():
    while True:
        print("ssh to what port? (Please enter a number)")
        port = input(">")
        print("\n")
        print(">ssh localhost -p %s" %(str(port)))
        if str(port) == "878":
            print("Success! ssh session connected to localhost on port %s" %(str(port)))
            return True
            input("Press enter to continue to next session.")
            return
        else:
            print("Error: Cannot connect ssh session to port %s, invalid port!" %(str(port)))
            input("Press enter to continue.")
            return



def nmap():
    while True:
        print("Use nmap to scan available ports? (y/n)")
        userinput = input(">")
        if userinput == "y":
            print("scanning available ports...")
            print(".")
            print(".")
            print("nmap has found these available ports open:")
            print("Port: 387/tcp Services: smtp")
            print("Port: 878/tcp Services: ssh")
            print("Port: 5301/tcp Services: unknown")
            input("press enter to continue")
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
        print("2. nmap")
        print("3. ssh")
        print("4. help")
        print(">")
        userinput = input()
        userinput = error_checking(userinput, 4)
        if userinput == 1:
            ls()
        if userinput == 2:
            nmap()
        if userinput == 3:
            if ssh() == True:
                return
        if userinput == 4:
            help.help(2)

def Main():

    print("You are logged in as Robin, Data Entry Supervisor")
    MainMenu()


if __name__ == '__main__':
    Main()