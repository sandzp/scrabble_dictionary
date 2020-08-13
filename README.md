# Scrabble Word Finding Dictionary

A command-line scrabble dictionary made in Python.

Can take up to 7 characters, and up to 2 wildcards.

Valid characters: A-Z, '*' or '?'. 

'scrabble.py' - raises exceptions when illegal characters written. Will exit the program and you will have to re-run. 

'scrabble2.py' - uses loops to handle error checking, program stays running until valid input entered. Do not have to re-run program. 

Utilizes the SOWPODS dictionary of words and has a scoring function to account for valid characters and wildcards. 

**How to use**

Needs both checking and scoring functions, SOWPODS dictionary all to be located in the same folder.

In command line, enter directory containing scripts and dictionary and after entering "Python3" input the characters you have directly after the "scrabble.py" call:

Example: Python3 "scrabble.py" AB?CKAP

Example 2: Python3 "scrabble2.py" achiBK

NB: Is generally pretty fast, but 5 characters and 2 wildcards may take > 1 minute to run. 
