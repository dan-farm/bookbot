def get_book_text(path):
        with open(path) as file:
            file_contents = file.read()
            return(file_contents)
        
def number_of_words(contents):
    contents =  len(contents.split())
    print(f"{contents} words found in the document")

def main():
    book_path = "books/frankenstein.txt"  
    full_text = get_book_text(book_path)
    number_of_words(full_text)

main()
