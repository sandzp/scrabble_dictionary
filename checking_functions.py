def input_sorter(arguments):
    '''
    This takes the input rack as a string, and returns a sorted list.
    This is important as the sort function moves "*" and "?" to the front, in that order.
    '''
    input_rack = []
    for x in arguments.lower():
        input_rack.append(x)
        input_rack.sort()
    return input_rack

def data_cutter(dataset, input_rack):
    '''
    Cut down dataset to only items <= length of input rack.
    '''
    data = []
    for item in dataset:
        if len(item) <= len(input_rack):
            data.append(item)
    return data

def wildcard_checker(words):
    '''
    Checks if wildcards are present.
    If single wildcard is present, creates 26 new lists of character permutations.
    If 2 wildcards are present it creates 276 new lists using itertools, representing every possible permutations of 2 letters.
    If no wildcards are present, it just outputs the original sorted input list.
    '''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_list = []
    if words[0] == '*' and not "?" in words:
        for item in alphabet:
            temp_list = words[1:]
            temp_list.insert(0,item)
            new_list.append(temp_list)
    elif words[0] == '?' and not "*" in words:
        for item in alphabet:
            temp_list = words[1:]
            temp_list.insert(0,item)
            new_list.append(temp_list)
    elif words[0] == '*' and words[1] == '?':
        from itertools import combinations_with_replacement
        combos = combinations_with_replacement(alphabet, 2)
        combos = list(combos)
        for item in combos:
            a, b = item
            temp_list = words[2::]
            temp_list.insert(0,a)
            temp_list.insert(1,b)
            new_list.append(temp_list)
    else:
        new_list = words
    return new_list

def character_dict(master):
    '''
    Convert a word into a dictionary (used for both match_words and wildcard_match functions).
    '''
    char_dict = {}
    for word in master:
        char_dict[word] = char_dict.get(word, 0) + 1
    return char_dict

def match_words(master_list, characters):
    '''
    For racks with no wildcards.
    Iterates through SOWPODS creating a dictionary for each word and compare letters in rack with it.
    Returns a single list of possible words.
    '''
    final_list = []
    for word in master_list:
        positive = 1
        word_dict = character_dict(word)
        for item in word_dict:
            if item not in characters:
                positive = 0
            elif word_dict[item] > characters.count(item):
                positive = 0
        if positive == 1:
            final_list.append(word)
            continue
    return final_list

def wildcard_match(master_list, wildcard_chars):
    '''
    For racks with wildcards.
    Iterates through all lists of possible letter combinations.
    In order for the word to be scored correctly, it creates a dictionary with a key:value pair of word:list it was generated from.
    '''
    final_list = []
    used_sublists = []
    for sublist in wildcard_chars:
        for word in master_list:
            word_dict = character_dict(word)
            positive = 1
            for item in word_dict:
                if item not in sublist:
                    positive = 0
                elif word_dict[item] > sublist.count(item):
                    positive = 0
            if positive == 1:
                final_list.append(word)
                used_sublists.append(sublist)
                continue
    final_dict = {final_list[i] : used_sublists[i] for i in range(len(final_list))}
    return final_dict
