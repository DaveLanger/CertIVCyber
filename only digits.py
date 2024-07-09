"""""
Author: DL
Date: 9/11/2022
Only Digits Function
onlydigits() receives a single string as its argument and returns a single string. The job of the function is to copy
all the digits (i.e. ‘0’ to ‘9’ characters) in the input string into the output string, removing all other characters.
"""
import string
import sys

#takes user input
input = sys.argv[1]

#defining function onlydigits()
def onlydigits(text):

    #removes punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    #removes letters
    text = text.translate(str.maketrans('', '', string.ascii_letters))

    return text

#calls only digits function
output_string = onlydigits(input)

#prints output
print(output_string)

# Test 1
result= onlydigits("123abct)*1")
if (result == '1231'):
    print('Test 1 OK')
else:
    print('Test 1 error: ' + result)

# Test 2
result= onlydigits("#$^%qqq77ww123abct)*1")
if (result == '771231'):
    print('Test 2 OK')
else:
    print('Test 2 error: ' + result)
