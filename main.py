# import sys module 
import sys 
# stats is the name of the file and count_words is the name of the function you want to import 
from stats import count_words
from stats import get_num_characters 
from stats import sort_dictionary
from stats import print_report

if len(sys.argv) == 2:

    def main():
        #file_path = "books/frankenstein.txt"
        text = get_book_text(sys.argv[1])        
        characters_result = get_num_characters(text)
        sort_list =sort_dictionary(characters_result)
        num_words=count_words(text)
        book_report = print_report(sys.argv[1], num_words, sort_list )
        return book_report

    def get_book_text(file_path):
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main()
