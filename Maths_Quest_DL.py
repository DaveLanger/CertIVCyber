#Author: DL
#Date: 08/10/2022
#Version: 3a

#Maths Quest Game
#A maths Game that allows a user to test their skills at times tables.

print("Welcome to Maths Quest!")

#get the player's name
name = input("Player 1: What's your name?")

#this input indicates which tables the player wishes to test, using integers between 1 & 12
choice_of_tables = int(input(name + ", Which times tables would you like to practice? (1-12)"))

#this instructs the user what to do and uses the name and choice_of_tables inputs.
print("Ok " + name + ": on a piece of paper, write down the " + str(choice_of_tables) + " times table from 1 to 12.  When you’re ready I’ll show you the answer so you can check your work.")

#sets a default value for userInput
userInput = "n"

#this while will keep looping until the user selects "y"
while userInput != "y":
    userInput= input("Are you ready? (Enter ‘y’ to start) ")


#for every integer between 1 and 12, inclusive, print the "choice_of_tables" + "x" + "the integer (all between 1&12)" + "=" "product of choice_of_tables and integers"
# e.g. 7 x 1 = 7, 7 x 2 = 14 and so on until you reach 12
for integer in range (1, 13):
    print(choice_of_tables, 'x', integer, '=', choice_of_tables*integer,)

#Ask the user if they got them all correct
correct = input("Did you get them all correct? (y/n)")

#if "y" - print great job, otherwise print better luck next time
if correct == 'y':
    print("Great job! Thank you for playing Maths Quest.")
else:
    print("Better luck next time. Thank you for playing Maths Quest.")
