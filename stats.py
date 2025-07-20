def number_of_words(contents):
    contents =  len(contents.split())
    return contents

def letter_count(text):
    characters = {} 
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    return characters

def sorted_letter_count(list_of_words):
    char_list = []
    for letter in list_of_words.items():
        char_dict = {"char": letter[0], "num": letter[1]}
        char_list.append(char_dict)
    char_list.sort(key=sort_on, reverse=True)
    return char_list  

def sort_on(items):
    return items["num"]