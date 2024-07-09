# WHILE loop example. Keep adding numbers
# until the user tells us to stop. The
# total variable accumulates the running sum.
# The num1 variable holds the latest number entered.
# The userInput variable holds the user's request to
# keep going (y) or not (something else)

# Start with nothing in the running sum,
# and with a dummy userInput value so that we
# enter the loop
total= 0
userInput = "y"

# While the user wants to keep going
while (userInput == "y"):
    num1 = int(input("Enter a number: "))
    # Add this to the running some
    total = total + num1
    # Find out if the user wants to loop back
    userInput = input("Continue (y/n)? ")
    
# We get here when the user didn't enter a "y", so the
# loop condition failed. Print out the sum
print("The total was", total)