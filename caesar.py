"""
Author: DL
Date: 08/11/2022
A simple encryption program that uses the Caeser Cipher to convert a plaintext message into cyphertext and back again
and vice versa. The program also sanitises user input before encrypting. This is done by converting all lower case
letters to uppercase, periods to the character "X" and removing all other punctuation. This program will show an error
if non ASCII characters are used.

An example of command line program usage is as follows;
{python caesar.py -1 "a dog"}
Which will show an output of {ZCNF}, which is all the letters of {a dog} shifted back one place
Please note that the input string should be encased in inverted commas.
"""

# importing string and sys libraries
import string
import sys

#read input string and shift value from the user
input_shift = sys.argv[1]
original_text = sys.argv[2]

"""The convert_to_Caesar function will take the user input and format/sanitise it into a state that is ready for encryption."""
def convert_to_Caesar(text):

    # change case to upper
    sanitised_input = text.upper()

    # remove spaces
    sanitised_input = sanitised_input.replace(" ", "")

    # convert period to "X"
    sanitised_input = sanitised_input.replace(".", "X")

    # remove numbers
    sanitised_input = sanitised_input.translate(str.maketrans('', '', string.digits))

    # "weed out" punctuation marks
    return sanitised_input.translate(str.maketrans('', '', string.punctuation))


#defines the ascii uppercase list
ascii_uppercase=list(string.ascii_uppercase)

#asssigning a value
printed_list=[]


"""The encrypt_Caesar function will take the converted text and encrypt / apply the input shift"""
def encrypt_Caesar(transformed_text):
    for character in transformed_text:

        # adds input shift to each character in text
        new_index = ascii_uppercase.index(character) + int(input_shift)

        # modulo converts numbers > 26 to < 26.
        new_index = new_index % 26

        #puts new index in a list
        printed_list.append(ascii_uppercase[new_index])
    return


#applies the convert_to_Caesar function to the original text
transformed_text = convert_to_Caesar(original_text)

#exception handling - if transformed text is still not ascii after cleansing it will exit
try:
    transformed_text.encode('ascii')
except UnicodeEncodeError:
    pass  # string is not ascii
    print("Please enter valid ascii characters and try again")
    sys.exit()
else:
    pass  # string is ascii

#applies the encrypt_Caesar function to the transformed list
output = encrypt_Caesar(transformed_text)

#removes spaces from the lists
output = ''.join(printed_list)

print(output)

