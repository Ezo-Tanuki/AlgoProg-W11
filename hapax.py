import os

def hapax(filename):
    file = open(f"{str(os.getcwd())}//{filename}")
    d = {} # initialize an empty dictionary
    s = "" # initialize an empty string

    fileData = file.read() # read file


    for letter in fileData: # loop through the letters
        if letter.isalpha(): # if the letter is an alphabets append the letter to the string
            s += letter
            continue
        
        if s.isspace(): # if the word is an empty string continue to the next letter
            continue
        
        # put the word to the dictionary if the next letter is not an alphabet
        s = s.lower() 
        d.update({s : d.get(s, 0) + 1})
        s = ""

    for word, value in d.items(): #print hapax
        if value == 1:
            print(word)

    print()
    print(d)

    file.close()