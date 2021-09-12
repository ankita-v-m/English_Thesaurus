import json         # we need json library to deal with data which is in json format
from difflib import get_close_matches       # to get close matched word

data = json.load(open("data.json"))         # store data of json file in a variable 

def translate(w):                           
    w = w.lower()                           # User may enter a word in any case so convert entered word into lower case as our data is in lower case
    if w in data:                           # check if user input is available in our data set
        return data[w]
    elif w.title() in data:                 #if user entered "delhi" this will check for "Delhi" as well.
        return data[w.title()]
    elif w.upper() in data:                 #in case user enters words like USA or NATO
        return data[w.upper()]

    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
