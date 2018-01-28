# TODO:
#2. Populate directories with relevant files
#3. fix bugs, probably
#4. Populate directoreis with irrelevant files

#defining initial variables & dictionaries
userDirectory = "Home"
sshTargets = ["", "Hawk", "Robin", "Wren", "Eagle"]
SSH = False
Directories = {
  "Home" : {
    "Desktop" : {
          #populate me
          "someFile" : "This is a test file.",
          "anotherFile" : "This is another test",
          "oneMoreFile" : "Here's one more"
    },
    "Documents" : {
      #populate me
    },
    "Downloads" : {
      #populate me
    },
    "Emails" : {
      "New Systems" : "Hey, Ed here. We've just updated to a new system,and you don't have an account yet. For now, you can ssh into mine. Username: Ed@button.gov, password: password. Remember to use a better password when you make your own account though!"
      #populate me"
    },
    "Music" : {
      #populate me
    },
    "Pictures" : {
      #populate me
    },
    "Videos" : {
      #populate me
    }
  }
}


#Defining the input cleaning function
def inputCleaner(string, size):
  try:
    string = string.replace(".", "").strip()
    string = int(string)
    return string
  except ValueError:
    print("You must choose one of the number options!")
    return -1
  if (int(string) < 1) or (int(string) > size):
    print("You must choose one of the number options!")
    return -1
    
#Defining the help function
def commandInfo():
  helpInput = input("Which command would you like help with? \n1. ls \n2. cd \n3. cat \n4. ssh \n5. help \n >")
  helpInput = inputCleaner(helpInput, 5)
  if (helpInput == 1):
    print("Shows contents of current directory.")
  elif (helpInput == 2):
    print("Change location to a specified directory, up 1 level, or return to the Home directory") 
  elif (helpInput == 3):
    print("Displays contents of a specified file")
  elif (helpInput == 4):
    print("Connects to a different user / ip")
  elif (helpInput == 5):
    print("How did you get here if you don't know how to use help?")
    
#Defining the ls function
def ls():
  if (userDirectory == "Home"):
    print(list(Directories["Home"].keys()))
  else:
    print(list(Directories["Home"][userDirectory].keys()))

#defining the cd function
def cd():
  global userDirectory
  if (userDirectory == "Home"):
    directoryChoice = input("Which directory should I move to? \n1. .. \n2. Desktop \n3. Documents \n4. Downloads \n5. Emails \n6. Music \n7. Pictures \n8. Videos \n>")
    directoryChoice = inputCleaner(directoryChoice, 8)
    if (directoryChoice >= 2):
      userDirectory=list(Directories["Home"].keys())[(directoryChoice-2)]
    elif (directoryChoice == 1):
      print("You do not have access to that directory.")
  else:
    directoryChoice = input("Which directory should I move to? \n1. .. \n>")
    directoryChoice = inputCleaner(directoryChoice, 1)
    userDirectory = "Home"
    
#defining the cat function
def cat():
  if (userDirectory == "Home"):
    print("No files to cat.")
  else:
    listOfFiles = list(Directories["Home"][userDirectory].keys())
    print("Which file would you like to cat?")
    for x in range(len(listOfFiles)):
      print(str(x+1) + ". %s\n" % listOfFiles[x])
      tmp = x
    catChoice = input("> ")
    catChoice = inputCleaner(catChoice, (tmp+1))
    print(Directories["Home"][userDirectory][listOfFiles[(catChoice-1)]])

#defining the ssh function
def ssh():
  sshTarget = input("Who do you want to SSH into? \n1. Hawk \n2. Robin \n3. Wren \n4. Eagle \n>")
  sshTarget = inputCleaner(sshTarget, 4)
  sshPassword = input("What is %s's password?" % sshTargets[sshTarget])
  if (sshTarget == 2 and sshPassword == "password"):
    global SSH
    SSH = True

#Game Loop
def main():
  while (SSH is False):
    command = input("What should I do? \n1. ls \n2. cd \n3. cat \n4. ssh \n5. help \n>")
    command = inputCleaner(command, 5)
    if (command == 1):
      ls()
    elif (command == 2):
      cd()
    elif (command == 3):
      cat()
    elif (command == 4):
      ssh()
    elif (command == 5):
      commandInfo()
      
if __name__ == "__main__":
  main()