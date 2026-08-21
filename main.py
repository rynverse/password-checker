import re
import os # This is used to save files
import hashlib


def checkPassword(userPassword):
    numberMultiplier = 2
    specialCharacterMultiplier = 3

    # Check for Special Characters
    checkSpecialCharacters = re.findall("[^a-zA-Z0-9]",userPassword)

    # Check for Numbers
    checkNumbers = re.findall("[0-9]", userPassword)

    # Check for English Characters
    checkCharacters = re.findall("[a-zA-Z]", userPassword)

    securityScore = len(checkCharacters) + (numberMultiplier * len(checkNumbers)) + (specialCharacterMultiplier * len(checkSpecialCharacters))
    print(f"The password security score is: {securityScore}")

    # Hash the password
    encodedPass = userPassword.encode('utf-8')
    hashedPass = hashlib.sha256(encodedPass).hexdigest()

    saveSecurityScore(securityScore,hashedPass)


def saveSecurityScore(securityScore,hashedPass):
    print("Saving security score..") 
    dirName = "security_score"

    # Makes Directory
    try:
        os.mkdir(dirName)
        print(f'Directory {dirName} created successfully!')
    except FileExistsError:
        print(f'Directory {dirName} already exists! Updating score file..')
    except PermissionError:
        print(f'Permission denied, unable to create {dirName} directory.')
    except Exception as e:
        print(f'An error occured: {e}')


    # Saves scores
    with open("security_score/securityScores.txt", "a") as file:
        file.write(f"\nSecurity Score: {securityScore}")
        file.write(f"\n Hashed Password: {hashedPass}")


## Main Code
checkPassword(input("Please enter password to be tested: "))


