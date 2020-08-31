# Title: Finding a Zipcode in the Digits of Pi
# Filename: main.py
# External files used: N/A
# External files created: N/A
# Author(s): Jared Diehl (jmddnb@umsystem.edu)
# Course: CMPSCI4500-001
# Date: 8/31/20
# Description: Outputs the digits of the user's zipcode in the first 1 million digits of Pi.
# Sources used:
#     https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py
#         Adapted the `calcPi` function to generate the digits of Pi up to a specified limit.

# GLOBAL VARIABLES
# Represents the maximum amount of digits of Pi to generate.
DIGITS_COUNT_MAX = 1000000
# Represents the fixed zipcode length.
ZIPCODE_LENGTH = 5

# Generates the digits of Pi up to a specified limit
def calcPi(limit):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            yield n
            if decimal == counter:
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

# The main function of this program
def main():
    # Loops until the user has input a number of length `ZIPCODE_LENGTH`
    while True:
        # Prompt the user for a zipcode of length `ZIPCODE_LENGTH`
        userInput = input("Enter a zipcode ({} digits): ".format(ZIPCODE_LENGTH))
        
        # Attempt to convert the user's input to an integer
        try:
            # Convert the user's input to an integer
            int(userInput)
            
            # Check the user's input length against `ZIPCODE_LENGTH`
            if len(userInput) != ZIPCODE_LENGTH:
                # Tell the user to try again because their input was not `ZIPCODE_LENGTH` digits in length
                print("Try again, not {} digits!".format(ZIPCODE_LENGTH))
            else:
                # If the user has input a number of length `ZIPCODE_LENGTH`, then stop asking them
                break
        except:
            # Tell the user to try again because their input was not a number
            print("Try again, not a number!")

    # References the generated digits of Pi
    digits = calcPi(DIGITS_COUNT_MAX)
    # Remembers the current digit's index being accessed of Pi
    currentDigitIndex = 1
    # Remembers the current index being accessed of the user's input
    currentZipcodeIndex = 0

    # Iteratively loop through the digits of Pi until a match of the user's input is found
    for digit in digits:
        # Check the current digit against the user's input using the current index
        if str(digit) == userInput[currentZipcodeIndex]:
            # Increment the zipcode index
            currentZipcodeIndex += 1
        else:
            # Reset the zipcode index
            currentZipcodeIndex = 0
        
        # Check `currentZipcodeIndex` against `ZIPCODE_LENGTH`
        if currentZipcodeIndex == ZIPCODE_LENGTH:
            # Tell the user the digit the zipcode first appears in Pi
            print("Found zipcode starting at digit #{} in Pi.".format(currentDigitIndex - ZIPCODE_LENGTH + 1))
            # Stop the program
            return
        
        # Increment the digit index
        currentDigitIndex += 1
    
    # Tell the user that the zipcode wasn't found
    print("Unable to find zipcode in first {} digits of Pi.".format(DIGITS_COUNT_MAX))

# Check to see if this file is explicitly executed.
if __name__ == "__main__":
    # And if so, then start the program.
    main()