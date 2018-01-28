
def ls():
    print("battleship")
    print("button-pushers.bin")
    print("steely-eye-security.readme")
    print("yo-mammas-cookbook")
    print("secplus.bin \n")

    input("Press enter to continue \n")

def cat():
    print("cat what?")
    file_to_read=input(">")
    if file_to_read == "steely-eye-security.readme":
        print("Steely eye security, the company that lets you keep that wary, watchful glazed eye on your employees \n"
              "like and old salty sea dog staring at you from the bridge. \n"
              "Make your employess wary that you watch their every movement \n"
              "Steely Eye secruity - cameras that stare so hard you can't tell if it's a soul-piercing gaze or a glass eye.\n"
              "\n"
              "To spy on the button pushers. Execute the secplus.bin file")
    if file_to_read == "button-pushers.bin":
        insecure_password = input("What's the password?")
        if insecure_password == "stickynote123":
            print("Camera view enabled \n")
        else:
            print("Try again \n")
    input("Press enter to continue \n")

def main_menu():
    print("What should I do?")
    print("1. ls")
    print("2. cat")
    print("3. cd")
    print("4. ssh")
    print("5. help \n")
    command = input(">")
    command = error_checking(command, 5)
    if command == -1:
        return
    if command == 1:
        ls()
    if command == 2:
        cat()


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



def Main():
    while True:
        main_menu()


if __name__=="__main__":
    Main()

