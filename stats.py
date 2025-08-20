# New function that accepts the text from the book as a string
# And returns the number of words in the string.
#.split()method
#Print the number of words to the console ? 
def count_words(text):
    return len(text.split())


# New function that takes the text from the book as a string 
# Returns the number of times each character, (including symbols and spaces), appears in the string.
# Convert any character to lowercase using the .lower() method, we don't want duplicates.
# Use a dictionary of String -> Integer. The returned dictionary should look something like this:
def get_num_characters(text):
    characters_dict = {}
    get_words = text
    for word in get_words:
        for character in word.lower():
            if character in characters_dict:
                characters_dict[character] += 1 
            else:
                characters_dict[character] = 1
    return characters_dict  
