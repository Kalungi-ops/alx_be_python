#propmpt user input
while True:
    try: 
        integer = int(input("Enter the size of the pattern: "))

        #check for positive integer
        if integer > 0:
            break
        else:
            print("Please enter a postive integer")
    except ValueError:
        print(f"Invalid input: {integer} is not a valid input. Please try again")

row_count = 0
while row_count < integer:
    for column in range(integer):
        #print an asterisk followed by end="" to keep it on the same line
        print("*", end="")
    print()
    #increment row count to prevent an infinite loop
    row_count += 1