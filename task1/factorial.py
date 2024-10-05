def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    Factorial of 0 is 1.
    
    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.
    
    Returns:
    int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
test_number = 5
print(f'The factorial of {test_number} is {factorial(test_number)}.')

# Test cases
print("\nRunning Factorial Calculation:")
print(f'Factorial of 0: {factorial(0)}')
print(f'Factorial of 1: {factorial(1)}')
print(f'Factorial of 5: {factorial(5)}')
print(f'Factorial of 6: {factorial(6)}')
