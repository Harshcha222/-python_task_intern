def fibonacci(n):
    """
    Returns the first n numbers of the Fibonacci sequence.
    """
    fib_sequence = [0, 1]  # Start with the first two numbers
    if n == 1:
        return [0]
    if n == 2:
        return fib_sequence
    
    # Generate Fibonacci numbers until the nth one
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
    return fib_sequence

# Example usage and test case
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
