# Ryn's Password Strength Checker

### Overview
I made this custom Python script to learn more about hashing in Python as well as file handling too. This script takes a text input to determine the strength of a given password, by using the following calculation:

`number of characters * respective multiplier` 

This gets the "score" of the password, which is then translated into strong/medium/weak..
The score, grading and a hashed version of the password is then saved in the `securityScores.txt` file within the `security_score` directory.

### Limitations
Currently (this may be improved in the future), the password checker does not account for patterns in the given password. This mean phrases such as `aaaaaaaaaaaaaaaaaaaaaaaaa` could get a score of **25** even if they are not necessarily secure. 

This is an active work in progress (as of 21/08/2026) and I will be exploring ways in which to improve this until I am fully satisfied with its state.