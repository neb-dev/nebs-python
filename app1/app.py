# import json
# data = json.load(open("data.json")) - the result will be stored in a python dictionary data type

# import difflib
# from difflib import SequenceMatcher
# SequenceMatcher(None, "rainn", "rainn").ratio() - None is used in place of IsJunk parameter which requires a function
# import get_close_matches
# get_close_matches("rain", data.keys())[0]
# - will return a list with three most similar words with cutoff similiary ratio default of 0.6,
# [0] returns the first word in the list (having the greatest similarity ratio)
import json
from difflib import get_close_matches

data = json.load(open("app1/data.json"))

def word_search(key):
    word = key.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        is_word = input("did you mean %s? y or n: " % get_close_matches(word, data.keys())[0])
        if is_word == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif is_word == "n":
            return "word not found"
        else:
            return "input not valid"    
    else:
        return "word not found"

input_word = input("enter a word: ")

result = word_search(input_word)

if isinstance(result, list):
    for definition in result:
        print(definition)
else:
    print(result)