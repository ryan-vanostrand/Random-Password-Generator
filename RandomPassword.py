#Ryan Van Ostrand
#Random Password Generator that gives a password rating and stores the passwords to a file of your choice. All files must be .txt.

#importing necessary components
import random
import string
#creating the file
fileName = input("What would you like the name of your secret stash to be?\n")
fileName = fileName + ".txt"
file1 = open(fileName, "a")
#instantiating strength compents
characters = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
special = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#Requesting an App
program = input("Insert the program you need a new password for and 'done' when you're done.\n")
#loop for password creating
while program != "done":
  #getting user input
  username = input("Insert your username.\n")
  length = int(input("How long do you want your password\n"))
  #creating password
  password = []
  for i in range(length):
    password.append(random.choice(characters))
  #resetting counts for strength checking
  countLower = 0
  countUpper = 0
  countSpecial = 0
  countNumber = 0
  #strength checking by different kinds of characters
  for i in range(length):
    if password[i] in lowercase and countLower == 0:
      countLower+= 1
    if password[i] in uppercase and countUpper == 0:
      countUpper+= 1
    if password[i] in number and countNumber == 0:
      countNumber+= 1
    if password[i] in special and countSpecial == 0:
      countSpecial+= 1
  sum = countLower + countUpper + countNumber + countSpecial
  #giving the strength rating
  if sum == 1 or length < 8:
    print("your password is weak")
  elif sum == 2:
    print("your password is moderate")
  elif sum == 3:
    print("your password is strong")
  else:
    if length < 20:
      print("your password is amazing")
    else:
      print("your password is emmaculate")
  #putting the password in string format
  password = ''.join(password)
  #Writing to the output file
  file1.write('Program: ' + program + "\nUsername: " + username + '\nPassword: ' + password + '\n')
  #asking for input again
  program = input("Insert the program you need a new password for and 'done' when you're done.\n")
#closing the file, giving access back to the machine.
file1.close()
