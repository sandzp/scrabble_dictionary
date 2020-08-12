# Import modules to be used in program

import sys
from checking_functions import *
from scoring_functions import *

# Open Dictionary

with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    sowpods = [datum.strip('\n').lower() for datum in raw_input]

# Illegal characters and scoring dictionary

illegal_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '+', ',', '-', '.', '/', ':', ';', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

# Initial input from command line

o = sys.argv

# Input validity Checking

class Error(Exception):
    """Base class for other exceptions"""
    pass

class SysLenError1(Error):
    """If no rack entered during initial input."""
    pass

class SysLenError2(Error):
    """If space used in initial input."""
    pass

class LenError1(Error):
    """If space used in initial input."""
    pass


illegal_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '+', ',', '-', '.', '/', ':', ';', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']

try:
    o = sys.argv
    if len(o) == 1:
        raise SysLenError1
    if len(o) > 2:
        raise SysLenError2
except SysLenError1:
    print("You didn't enter a rack, please re-run and enter a rack of valid characters.")
    sys.exit()
except SysLenError2:
    print("No spaces permitted, please re-run and enter a rack without spaces and valid characters.")
    sys.exit()
else:
    a = (sys.argv[1]).strip('""')

try:
    if len(a) < 2 or len(a) > 7:
        raise LenError1
    else:
        pass
except LenError1:
    print("You must only enter between 2-7 legal characters. Please re-run program.")
    sys.exit()
else:
    pass

try:
    for letter in a:
        if letter in illegal_characters:
            raise ValueError
except ValueError:
    print("You entered an invalid character, only letters, '*', and '?' are allowed. Please re-run program.")
    sys.exit()
else:
    pass

try:
    for letter in a:
        if a.count('*') > 1:
            raise ValueError
except ValueError:
    print("Only one of each wildcard character is allowed. Please re-run program.")
    sys.exit()
else:
    pass

try:
    for letter in a:
        if a.count('?') > 1:
            raise ValueError
except ValueError:
    print("Only one of each wildcard character is allowed. Please re-run program.")
    sys.exit()
else:
    pass

# Matching processes

b = input_sorter(a)

data = data_cutter(sowpods, b)

c = wildcard_checker(b)

if '*' in b and not '?' in b:
    d = wildcard_match(data, c)
elif '?' in b and not '*' in b:
    d = wildcard_match(data, c)
elif '*' and '?' in b:
    d = wildcard_match(data, c)
else:
    d = match_words(data, c)

# Scoring Processes

if '*' in b and not '?' in b:
    e = wildcard_scorer(d, b)
elif '?' in b and not '*' in b:
    e = wildcard_scorer(d, b)
elif '*' and '?' in b:
    e = wildcard_scorer(d, b)
else:
    e = score_word(d)

# Print outputs

for item in e:
    print('({0}, {1})'.format(item[0],item[1]))
