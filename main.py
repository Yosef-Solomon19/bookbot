def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)    
    print(f"{count_words(text)} words found in the document")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

# New function that accepts the text from the book as a string
# And returns the number of words in the string.
#.split()method
#Print the number of words to the console ? 
def count_words(text):
    return len(text.split())


main()
