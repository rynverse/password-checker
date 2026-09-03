import re # Regex
import os # This is used to save files
import hashlib # For hashing
import requests # Used to send API Request


def checkPassword(userPassword):
    # Multipliers
    repeatedCharacterMultiplier = 1
    numberMultiplier = 2
    specialCharacterMultiplier = 3
    trailingCharacterMultiplier = 4
    breachedMultiplier = 100


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

    # Additions for security score
    securityScore = len(checkCharacters) + (numberMultiplier * len(checkNumbers)) + (specialCharacterMultiplier * len(checkSpecialCharacters)) + len(checkTrailingCharacters * trailingCharacterMultiplier)
    # Subtractions for security score
    securityScore -= len(checkRepeatedCharacters * repeatedCharacterMultiplier)

    # Hash the password and compare it to pwnedpasswords API
    encodedPass = userPassword.encode('utf-8')
    hashedPass = hashlib.sha1(encodedPass).hexdigest().upper() # Upper as pwnedpasswords returns in capital letters
    prefix = hashedPass[:5]
    suffix = hashedPass[5:]

    # Explanation:
    # The API takes in the PREFIX of the hashed password, and returns matching SUFFIXES, alongside how many breaches
    # We also need to remove the breach count 
    matches = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}") # Returns hashes that are similar, now we manually check
    returnedSuffixes = set()
    for line in matches.text.splitlines(): # Seperates the breach count from the response
        parts = line.split(":")
        returnedSuffixes.add(parts[0])

# Checks if the password is breached
    if suffix in returnedSuffixes: 
        breached = True
        securityScore -= breachedMultiplier
    else:
        breached = False
    
    
    ## Score Breakdown
    print("Score Breakdown: ")
    print(f" English Characters: {len(checkCharacters)} ({len(checkCharacters)})")
    print(f" Numbers: {len(checkNumbers)} ({len(checkNumbers * numberMultiplier)})")
    print(f" Special Characters: {len(checkSpecialCharacters)} ({len(checkSpecialCharacters * specialCharacterMultiplier)})")
    print(f" Trailing Characters: {len(checkTrailingCharacters)} ({len(checkTrailingCharacters * trailingCharacterMultiplier)})")
    print(f" Repeated Characters: {len(checkRepeatedCharacters)} ({len(checkRepeatedCharacters)* repeatedCharacterMultiplier})")
    print(f" Has this password been breached? {breached}")
    print(f"The password security score is: {securityScore}")

    saveSecurityScore(securityScore,hashedPass)


def saveSecurityScore(securityScore,hashedPass):
    # Compares security score to predetermined values
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


