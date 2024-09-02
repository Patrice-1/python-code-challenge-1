#An even function_that takes a single parameter called number and returns True if its even

def is_even(number):
    #check if the number is divisible by 2 and return True if it is
    return number % 2 == 0

#test the function with a number
print(is_even(10))
print(is_even(11))
