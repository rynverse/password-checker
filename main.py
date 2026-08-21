import re
import os # This is used to save files


def checkPassword(userPassword):
    # Check for Special Characters
    checkSpecialCharacters = re.findall("[^a-zA-Z0-9]",userPassword)

    # Check for Numbers
    checkNumbers = re.findall("[0-9]", userPassword)

    # Check for English Characters
    checkCharacters = re.findall("[a-zA-Z]", userPassword)

    # Debug Code
    print(len(checkSpecialCharacters))
    print(len(checkNumbers))
    print(len(checkCharacters))

    securityScore = (len(checkSpecialCharacters) * 3) + (len(checkNumbers) * 2) + (len(checkCharacters * 1))
    print("The password security score is: ") + str(securityScore)


## Main Code
checkPassword(input("Please enter password to be tested: "))


