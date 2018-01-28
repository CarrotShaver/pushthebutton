#	TODO:
#1. Make cat function, probably by using values associated with keys under the various directories
#2. Make ssh function, don't know how yet
#3. Populate directories with relevant files
#4. Populate directoreis with irrelevant files
#5. fix bugs, probably
import help
#defining initial variables & dictionaries
userDirectory = "Home"
Directories = {
	"Home" : {
		"Desktop" : {
        	#populate me
		},
		"Documents" : {
			#populate me
		},
		"Downloads" : {
			#populate me
		},
		"Emails" : {
			#populate me
			#email for progressing: "Hey, Ed here. We've just updated to a new system,and you don't have an account yet.
			#For now, you can ssh into mine. Username: Ed@button.gov, password: password. 
			#Remember to use a better password when you make your own account though!"
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

    
#Defining the ls function
def ls():
  if (userDirectory == "Home"):
    print(Directories["Home"].keys())
  else:
    print(Directories["Home"][userDirectory])

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
    print("to be implemented")
	#probably get the value associated with keys inside of directories.

#defining the ssh function
def ssh():
    print("to be implemented")
	#Not sure how to implement this yet

#Game Loop
def main():
  while True:
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
      help.help(1)
      
main()