#Author: DL
#Date: 08/10/2022
#Version: 1e

#Guess the random number game
#One player vs. the computer

#Import the random number generator module
import random

#Stating guesses range
minGuess = 1
maxGuess = 6

#Ask the user for their name and their guess
name = input("What is your name? ")
print("Hi " + name)
print("Enter a number between: " + str(minGuess) + " and " + str(maxGuess))
guess = int(input("What is your guess?"))

#Generate a random number, tell the user if they won or lost and what the random number was.
secretNumber = random.randint(minGuess, maxGuess)
if guess == secretNumber:
    print("Congratulations, you got it right!")
else:
    print("You lose - the number was " + str(secretNumber) + "")

print("Thank you for playing Guess the Number.")
