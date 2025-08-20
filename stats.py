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
    get_words = text.lower().split()
    for word in get_words:
        print(word)
        for character in word:
            print(character)
            if character in characters_dict:
                characters_dict[character] += 1 
            else:
                characters_dict[character] = 1
    print(characters_dict)

    
get_num_characters("Waffles Yyosef")