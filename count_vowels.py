#function that takes a string of type text as input and returns the count of vowels(a, e, i, o, u) in the string ignoring case sensitivity.

def count_vowels(text):
    #create a set of vowels
    vowels = set('aeiou')

    #remove non-alphabetic characters and convert the text to lowercase
    text = ''.join(filter(str.isalpha, text)).lower()
    
    #convert the text to lowercase and count the occurrences of vowels
    return sum(1 for char in text if char in vowels)

#test the function with a string
print(count_vowels("Hello Python!"))
print(count_vowels("HELLO"))
print(count_vowels("54757!!!!!</>"))