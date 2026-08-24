# Ryn's Password Strength Checker

### Overview
I made this custom Python script to learn more about hashing and file handling in Python, as well as (unintentionally) learning more about Regular Expressions. This script takes a text input to determine the strength of a given password, by using the following calculation:

`number of characters * respective multiplier ± (special condition * special modifier)` 

This gets the "score" of the password, which is then translated into strong/medium/weak..
The score, grading and a hashed version of the password is then saved in the `securityScores.txt` file within the `security_score` directory. A breakdown of the score is also provided in the terminal, and may also be added mto the `securityScores.txt` file in the future, if needed.

### Limitations
Currently, this password checker has no way of identifying commonly used passwords and accounting for them.

This is an active work in progress (as of 24/08/2026) and I will be exploring ways in which to improve this until I am fully satisfied with its state.

