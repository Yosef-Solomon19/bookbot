# stats is the name of the file and count_words is the name of the function you want to import 
from stats import count_words

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)    
    print(f"{count_words(text)} words found in the document")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()
