def print_upper_words(words,chars):
    for word in words:
        for char in chars:
            if(char == word[0]):
                print(word.upper())

    



print_upper_words(["hello", "hey", "goodbye","ben","ccccc", "yo", "yes"],{"h", "y"})

