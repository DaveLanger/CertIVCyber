#Author: DL
#Date: 08/10/2022
#Version: 2b

#Rock Paper Scissors Game
#A Two Players Rock Paper scissors game

print("Welcome to Rock, Paper, Scissors!")
print("Let's Begin...")

#the input asks for player names
name1 = input("Player 1: What's your name?")
name2 = input("Player 2: What's your name?\n")

print("Hello " + name1 + " and " + name2)
print(name2 + " : Close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n" )
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

#adds some line spacing for readability
print(" \r ")

#states the conditions where player 2,aka "name2", wins.
if choice1 == 'r' and choice2 == 'p':
    print(name2 + " wins! ")
elif choice1 == 'p' and choice2 == 's':
    print(name2 + " wins! ")
elif choice1 == 's' and choice2 == 'r':
    print(name2 + " wins! ")

#states the conditions where player 1, aka "name1", wins.
elif choice1 == 'p' and choice2 == 'r':
    print(name1 + " wins! ")
elif choice1 == 's' and choice2 == 'p':
    print(name1 + " wins! ")
elif choice1 == 'r' and choice2 == 's':
    print(name1 + " wins! ")


#states the conditions where it's a draw
elif choice1 == choice2:
    print("It's a draw!")

#adds some line spacing for readability
print(" \r ")


print("Thanks for playing Rock, Paper Scissors")


