# import json
# data = json.load(open("data.json")) - the result will be stored in a python dictionary data type
# data["rain"]
import json

data = json.load(open("app1/data.json"))

def word_search(key):
    return data[key]

input_word = input("enter a word: ")

print(word_search(input_word))