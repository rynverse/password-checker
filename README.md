# Ryn's Password Strength Checker

### Overview
This is a Python script that uses a scoring system based the number of characters/numbers and specific characteristics of a password, as well as comparing it to known breached password. I made this Python Script to learn more about file handling and Regular Expressions, however it grew into a much larger project which uses the `pwnedpasswords` API and `haslib`.

The scoring can be summarised as `score ± multiplier`

The current Multipliers are:
| Multiplier | Score | Description | 
| ------------- | ------------- | ------------- |
| `breachedMultiplier` | -100 | -100 score if the password was found in a breach |
| `repeatedCharacterMultiplier` | -1 | -1 Score per repeated character `aa` `bb` for example |
| `characterMultiplier` | +1 | +1 Score per character in the given password |
| `numberMultiplier` | +2 | +2 Score per number in the given password |
| `specialCharacterMultiplier` | +3 | +3 Score per special character (`!"£$%^&*()` for example) in the given password |
| `trailingCharacterMultiplier` | +4 | +4 Score per trailing special/capital character. For example `&s&` or `)bA` |

The script then sends the (uppercase) hashed password's prefix to the `pwnedpasswords` API, which returns the suffix of hashes that matched the prefix. The script then removes the number of times a password has been breached, and compares the hashes with the given password - to determine whether it has been breached. If it has been breached, the `breachedMultiplier` is subtracted from the score.

With the implementation of the `pwnedpasswords` API, I am currently happy with its functional state and have no current plans for future updates.

### Prerequisites
- Requires `pip`, see installation guide [here](https://pip.pypa.io/en/stable/installation/)
- Requires `requests` module (use the command `pip install requests`)

### What I learnt from this project
Initially, I had learnt how to save password scores to a new file/directory, which can be useful for dumping logs made in Python in the future (planned project) as well as learning about the various types of hashing like SHA-1. 

Hashing is incredibly useful for saving passwords as the hash is very hard to reverse, meaning a leak of a hash does not immediately lead to passwords being discovered. This is incredibly useful for authenticating users, as all you need to do to check the result of the hash function and compare it to the hash stored on the server to authenticate a user, if it matches. It is best practice to use modern hashing algorithms like SHA-256 or SHA-3 when storing passwords for example.

Furthermore, I learnt how to send `GET` requests using the `request` module in Python, and converting the given result back into something useful. This is incredibly useful knowledge, as APIs can be misused if not configured correctly and I am gaining an understanding of how they work - which may help in the cybersecurity field.

### Limitations
Password scoring is not a great way of identifying the strength of a password, and this project should not be treated as a way to properly see the strength of your password. There are more modern solutions that use entropy (randomness) to determine the strength of passwords, as well as using the above.