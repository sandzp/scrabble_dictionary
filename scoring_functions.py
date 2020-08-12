'''Scoring functions for both non-wildcard and wildcard racks'''

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def score_word(words):
    '''
    For non-wildcard racks, this function simply iterates through the list of possible words from SOWPODS and scores them according to Scrabble rules.
    Takes in argument: words, which is the list of possible SOWPODS words that can be made from the input rack.
    '''
    score_list = []
    for word in words:
        points = 0
        for letter in word:
            points += scores[letter]
        score_list.append((points, word))
    return sorted(score_list, key = lambda x: x[0], reverse = True)

def wildcard_scorer(wildcard_dict, original_input):
    '''
    This very long function takes in the dictionary of words generated form possible wildcard combos.
    It takes two arguments: the dictionary of words:letter combinations that have been generated from SOWPODS and the original input rack to determine how many wildcards were used.
    It iterates through the dictionary and utilizes constraints to score the words, and if necessary subtract scores if wildcards were utilized to form them.
    '''
    score_list = []
    if "*" in original_input and not "?" in original_input:
        for word, letters in wildcard_dict.items():
            if letters[0] in word:
                points = 0
                h = letters[0]
                h_val = scores.get(h)
                for character in word:
                    points += scores[character]
                score_list.append((points-h_val, word))
            else:
                points = 0
                for character in word:
                    points += scores[character]
                score_list.append((points, word))
    elif "?" in original_input and not "*" in original_input:
        for word, letters in wildcard_dict.items():
            if letters[0] in word:
                points = 0
                h = letters[0]
                h_val = scores.get(h)
                for character in word:
                    points += scores[character]
                score_list.append((points-h_val, word))
            else:
                points = 0
                for character in word:
                    points += scores[character]
                score_list.append((points, word))
    elif "*" and "?" in original_input:
        for word, letters in wildcard_dict.items():
            if letters[0] in word and not letters[1] in word:
                points = 0
                h = letters[0]
                h_val = scores.get(h)
                for character in word:
                    points += scores[character]
                score_list.append((points-h_val, word))
            elif letters[1] in word and not letters[0] in word:
                points = 0
                h = letters[0]
                h_val = scores.get(h)
                for character in word:
                    points += scores[character]
                score_list.append((points-h_val, word))
            elif letters[0] and letters[1] in word:
                if letters[0] in word and not letters[1] in word:
                    points = 0
                    h = letters[0]
                    h_val = scores.get(h)
                    for character in word:
                        points += scores[character]
                    score_list.append((points-h_val, word))
                elif letters[1] in word and not letters[0] in word:
                    points = 0
                    h = letters[0]
                    h_val = scores.get(h)
                    for character in word:
                        points += scores[character]
                    score_list.append((points-h_val, word))
                elif letters[0] and letters[1] in word and letters[0] == letters[1]:
                    points = 0
                    h = letters[0]
                    h_val = scores.get(h)
                    for character in word:
                        points += scores[character]
                    score_list.append((points-h_val, word))
                else:
                    points = 0
                    h = letters[0]
                    i = letters[1]
                    h_val = scores.get(h)
                    i_val = scores.get(i)
                    for character in word:
                        points += scores[character]
                    score_list.append(((points-(h_val+i_val)), word))
            else:
                points = 0
                for character in word:
                    points += scores[character]
                score_list.append((points, word))
    return sorted(score_list, key = lambda x: x[0], reverse=True)
