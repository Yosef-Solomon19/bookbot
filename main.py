# stats is the name of the file and count_words is the name of the function you want to import 
from stats import count_words
from stats import get_num_characters 
from stats import sort_dictionary

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)        
    characters_result = get_num_characters(text)
    #print(f"{count_words(text)} words found in the document, {characters_result}")
    sort_dictionary(characters_result)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()
