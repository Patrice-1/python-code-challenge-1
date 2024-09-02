#function named calculate_factorial that takes a non-negative integer n as input and returns the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.

def calculate_factorial(n:int) ->int:
    #base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    
    #recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * calculate_factorial(n-1)

#test the function with a number
print(calculate_factorial(5))
print(calculate_factorial(4))
print(calculate_factorial(0))
