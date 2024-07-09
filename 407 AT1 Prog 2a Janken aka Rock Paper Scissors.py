#Author: DL
#Date: 08/10/2022
#Version: 1b

#Rock Paper Scissors Game
#Two Players

print("Welcome to Rock, Paper, Scissors!")
print("Let's Begin...")
name1 = input("Player 1: What's your name?")
name2 = input("Player 2: What's your name?\n")

print("Hello " + name1 + " and " + name2)
print(name2 + " : Close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n" )
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

if choice1 == 'r' and choice2 == 'p':
    print("Is this working????")


else:
    print("Thanks for playing Rock, Paper Scissors")


