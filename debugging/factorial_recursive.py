#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given integer using recursion.
    
    Parameters:
    - n: An integer for which the factorial is to be calculated.
    
    Returns:
    Returns the factorial of the input integer 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Take the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)

