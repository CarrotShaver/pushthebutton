import time
import help

def email(index):
    if index == 0:
        print("")
        print("")
        print("")
    if index == 1:
        print("")



def nmap():
    while True:
        print("Use nmap to scan available ports? (y/n)")
        input = input()
        if input == y:
            print("scanning available ports...")
            time.delay(1)
            print(".")
            time.delay(1)
            print(".")
            time.delay(1)
            print("nmap has found these available ports open:")
            print("Port: 53017")
            print("Port: 3878")
            print("Port: 8789")
        if input == n:
            return


def cat():


    def ssh():




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
        while (true):
            print("What Should I Do?")
            print("1. ls")
            print("2. cd")
            print("3. cat")
            print("4. nmap")
            print("5. ssh")
            print("6. help")
            input = input(">")
            input = error_checking(input, 5)
            if input == 1:
                ls()
            if input == 2:
                cd()
            if input == 3:
                cat()
            if input == 4:
                nmap()
            if input == 5:
                ssh()
            if input == 6:
                help(2)

    def Main():
        MainMenu()


    if __name__ == '__main__':
        Main()

