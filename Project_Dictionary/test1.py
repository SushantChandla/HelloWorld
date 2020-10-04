import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def finder(word):
    word=word.lower()
    if word in data:                      #direct matching of the word
        return data[word]
    elif word.title() in data:           #Making first letter capital for Proper Nouns
        return data[word.title()]
    elif word.upper() in data:           #searching for shortforms by making all caps
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0 :     #finding close matches for the entered word 
        choice=input("Did you mean %s instead of %s. Enter Yes(Y) or No(N)??" %(get_close_matches(word,data.keys())[0],word))
        if choice=="Y":        #To use that close match
            return data[get_close_matches(word,data.keys())[0]]
        elif choice=="N":       #Don't use that close match'
            return "No  word like %s exists!!!" % word
        else:               #entered something else not matching to Y or N
            return "You dumb there is no choice like that!!!"
    else:          #No close matches found ie no existence
        return  "The word you entered does not exist in the Dictionary"

w=input("Enter word: ")

answer=finder(w)           #!To give a user friendly output instead of showing a list
if type(answer)==list:    #above return statments also have strings
    for i in answer:
        print(i)
else:
    print(answer)        #directly printing the strings