from stats import *
import sys

def get_book_text(path):
        with open(path) as file:
            file_contents = file.read()
            return(file_contents)
        
def main():
    args = sys.argv
    if len(sys.argv) > 1:
        book_path = args[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    full_text = get_book_text(book_path)
    word = letter_count(full_text)
    number = number_of_words(full_text)
    sorted = sorted_letter_count(word)  
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
main()
