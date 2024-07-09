#DL
#13/10/2022
#Program that prints asterisks in a rectangle. The user can input the size of the rectangle that is desired.
#The program will keep looping until a value of "0" is entered in the rows input.


# sets original value for variable
rows = 1
columns = 1

#if rows = 0, will exit the program
while rows != 0:

        #rows input
        rows = int(input("How many rows (1-10, 0 to exit)?"))
        if rows <11 and rows >0:


            #columns input
            columns = int(input("How many columns (1-10)?"))
            if columns < 11 and columns > 0:



                #prints asterisks in rows x columns
                for integer in range(rows):
                    print("*" * columns)
                print("\n")

    #if number isn't between 0 and 10, will print "Invalid Number" and re loop
            else:
                    print("Invalid number")
        else:
            print("Invalid number")

#will exit if rows = 0
print("Thank you, goodbye!")
exit()