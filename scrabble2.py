# Import Modules

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

# Input validity checking

if len(o) == 1:
    while True:
        a = input("You didn't enter an input, please try again: ").strip('""')
        if len(a) < 2 or len(a) > 7:
            a = input("2-7 valid characters allowed. Please try again: ").strip('""')
            if len(a) >= 2 and len(a) <= 7:
                break
        else:
            break
elif len(o) > 2:
    while True:
        a = input("You entered too many arguments. Please try again: ").strip('"')
        if len(a) < 2 or len(a) > 7:
            a = input("2-7 valid characters allowed. Please try again: ").strip('""')
            if len(a) >= 2 and len(a) <= 7:
                break
        else:
            break
else:
    a = sys.argv[1]

if len(a) < 2 or len(a) > 7:
    while True:
        a = input("Only 2-7 valid characters allowed. Please try again: ").strip('""')
        if len(a) < 2 or len(a) > 7:
            continue
        else:
            break

for letter in a:
    if letter in illegal_characters:
        while True:
            a = input("You entered an illegal character. Please re-enter using only valid characters: ").strip('""')
            if len(a) < 2 or len(a) > 7:
                while True:
                    a = input("Only 2-7 valid characters allowed. Please try again: ").strip('""')
                    if len(a) >= 2 or len(a) <= 7:
                        break
                    else:
                        continue
            else:
                break

# Matching and Scoring Processes.

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
