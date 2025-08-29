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

#Part 1 
# Add a new function that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Create a new function that takes the dictionary of characters and their counts
# Initalize a empty list to be sorted
# Create for loop to get the key and value separately 
# Create dictionary inside the loop containing two key-value pairs and add them to the list

#Part 2
#If the character is not an alphabetical character just skip it. .isalpha() in the for loop.
#Sort the sorted_dict from greatest to least based on the count

def sort_dictionary(dictionary):
    sort_dict = []
    
    for key in dictionary:
        if key.isalpha():
            c_dict={}
            c_dict.update({'char': key, 'num': dictionary[key]})
            sort_dict.append(c_dict)
        else: 
            pass
    sort_dict.sort(reverse=True, key=sort_on)
    return sort_dict

    # return dictionary

#helper function 
def sort_on(item):
    return item["num"]