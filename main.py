import re # Regex
import os # This is used to save files
import hashlib


def checkPassword(userPassword):
    trailingCharacterMultiplier = 4
    specialCharacterMultiplier = 3
    numberMultiplier = 2
    repeatedCharacterMultiplier = -1


    # Check for Special Characters
    checkSpecialCharacters = re.findall("[^a-zA-Z0-9]",userPassword)

    # Check for Numbers
    checkNumbers = re.findall("[0-9]", userPassword)

    # Check for English Characters
    checkCharacters = re.findall("[a-zA-Z]", userPassword)

    # Special Case Checkers
    checkTrailingCharacters = re.findall("(?<=[0-9A-Z])[a-z](?=[0-9A-Z])", userPassword)

    # Check for Repeated Characters
    checkRepeatedCharacters = re.findall("(.)\1{2,2}", userPassword)

    ## Score Breakdown
    print("Score Breakdown: ")
    print(f" English Characters: {len(checkCharacters)} ({len(checkCharacters)})")
    print(f" Numbers: {len(checkNumbers)} ({len(checkNumbers * numberMultiplier)})")
    print(f" Special Characters: {len(checkSpecialCharacters)} ({len(checkSpecialCharacters * specialCharacterMultiplier)})")
    print(f" Trailing Characters: {len(checkTrailingCharacters)} ({len(checkTrailingCharacters * trailingCharacterMultiplier)})")
    print(f" Repeated Characters: {len(checkRepeatedCharacters)} ({len(checkRepeatedCharacters)* repeatedCharacterMultiplier})")

    # Can turn these into variables later.

    # Additions for security score
    securityScore = len(checkCharacters) + (numberMultiplier * len(checkNumbers)) + (specialCharacterMultiplier * len(checkSpecialCharacters)) + len(checkTrailingCharacters * trailingCharacterMultiplier)
    # Subtractions for security score
    securityScore -= len(checkRepeatedCharacters *repeatedCharacterMultiplier)
    print(f"The password security score is: {securityScore}")

    # Hash the password
    encodedPass = userPassword.encode('utf-8')
    hashedPass = hashlib.sha256(encodedPass).hexdigest()

    saveSecurityScore(securityScore,hashedPass)


def saveSecurityScore(securityScore,hashedPass):
    if securityScore < 5:
        print("Weak Password")
        strength = 1
    elif securityScore >=5 & securityScore < 10:
        print("Medium Strength Password")
        strength = 2 
    else:
        print("Strong Password")
        strength = 3
        
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
        file.write(f"\nSecurity Score: {securityScore}\n Strength: {strength}\n Hashed Password: {hashedPass}")


## Main Code
checkPassword(input("Please enter password to be tested: "))


