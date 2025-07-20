from stats import *

def get_book_text(path):
        with open(path) as file:
            file_contents = file.read()
            return(file_contents)
        
def main():
    book_path = "books/frankenstein.txt"  
    full_text = get_book_text(book_path)
    word = letter_count(full_text)
    number = number_of_words(full_text)
    sorted = sorted_letter_count(word)  
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
main()
