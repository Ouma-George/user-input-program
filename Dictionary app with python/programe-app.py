import json
import difflib

# Load dictionary data
def load_dictionary(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

#function to get word definition
def get_definition(word, dictionary):
    word = word.lower()  # Convert word to lower case to handle case insensitivity
    return dictionary.get(word, "Word not found in the dictionary.")

#function to suggest similar words
def suggest_similar_words(word, dictionary):
    word_list = list(dictionary.keys())
    suggestions = difflib.get_close_matches(word, word_list)
    return suggestions

#main function to tie everything together.
def main():
    # Load dictionary data
    dictionary_data = load_dictionary('C:/Users/User/Desktop/Python-PLP/Dictionary app with python/dictionary.json')
    
    # Get user input
    user_word = input("Enter a word: ").strip()
    user_word = user_word.lower()  # Convert input to lower case
    
    # Get definition
    definition = get_definition(user_word, dictionary_data)
    
    if definition == "Word not found in the dictionary.":
        # Suggest similar words
        suggestions = suggest_similar_words(user_word, dictionary_data)
        if suggestions:
            print(f"Word not found. Did you mean: {', '.join(suggestions)}?")
        else:
            print(definition)
    else:
        print(f"Definition: {definition}")

if __name__ == "__main__":
    main()

