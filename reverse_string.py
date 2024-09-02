#A function that takes a string of type text as input and returns the reversed version of it

def reverse_string(text):
    #split the string into a list of characters
    characters = list(text)
    
    #reverse the list of characters
    reversed_characters = characters[::-1]
    
    #join the reversed characters back into a string and return it
    return ''.join(reversed_characters)

#test the function with a string
print(reverse_string("Hello World!"))
print(reverse_string("Python is fun"))
