#import help

def battleship():
    from random import randint

    board = []

    for x in range(6):
        board.append(["O"] * 6)

    def print_board(board):
        for row in board:
            print((" ").join(row))

    print("Let's play Battleship!")
    print_board(board)

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(9):
        print("Turn"), turn
        guess_row = int(input("Guess Row:"))
        guess_col = int(
            input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                print("Oops, that's not even in the ocean.")
            elif (board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
        if turn == 8:
            print("Game Over")
        turn = + 1
        print_board(board)

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

    if file_to_read == "secplus.bin":
        print("Camera view enabled \n")
        print("""            &@.                                                 %@             
                    %                                                    .(            
                    %      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.     .(            
                    %    /*(                                      **(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    /*                                        *(    .(            
                    %    ./****************************************#,    .(            
                    %                                                    .(            
                    @                                                    @             
                        @..............................................@               
                       @                              ,,,,,,,,,,,,, .   @              
                       @                             ,password:    .    @
                       @              		         ,stickynote123.    @
                       @                             ,,,,,,,,,,,,,,.    @              
                       @                                                @              
                       @                                                @              
                       @                                                @              
                       @************************************************@              
            @&&  %  #   #  #  /,  (  *(  #  (   #  (   (  #    */**%  *   %  %   &     
           /@,****(*** **//** **//**,******/******,*** **//*****#**/(..,..*......,@    
           @**/,********* */*,********/******/ ****** **/.**,*******(,,,,,,.,,/,,,#@   
          @/((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((@  
          @                                                                         @  
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  

                                                                         #@@@@@@       
                                                                               *@      
                                                                        &********@""")

    if file_to_read == "button-pushers.bin":
        insecure_password = input("What's the password? \n")
        if insecure_password == "stickynote123":
            return 1
        else:
            print("Wrong answer \n")

    if file_to_read == "yo-mammas-cookbook":
        print("Add sriracha. Done.")


    if file_to_read == "battleship":
        battleship()

    input("Press enter to continue \n")
    return 0

def main_menu():
    while True:
        print("What should I do?")
        print("1. ls")
        print("2. cat")
        print("3. cd")
        print("4. ssh")
        print("5. help \n")
        command = input(">")
        command = error_checking(command, 5)
        if command == 1:
            ls()
        if command == 2:
            nextlevel = cat()
            if nextlevel == 1:
                return
        if command == 3:
            print("No other directories")
        if command == 4:
            print("ssh not enabled")
        if command == 5:
            help(3)

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
    main_menu()
    return


if __name__=="__main__":
    Main()

