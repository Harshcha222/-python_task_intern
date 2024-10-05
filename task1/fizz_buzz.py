def fizz_buzz(n):
    """
    Prints the numbers from 1 to n. 
    For multiples of three, prints "Fizz" instead of the number, 
    for multiples of five, prints "Buzz", 
    and for multiples of both three and five, prints "FizzBuzz".
    
    Parameters:
    n (int): The upper limit of the range to print.
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  
        elif i % 3 == 0:
            print("Fizz") 
        elif i % 5 == 0:
            print("Buzz")  
        else:
            print(i)  

# Example usage
fizz_buzz(15)

# Add test cases as print statements
print("\nRunning FizzBuzz with n = 15:")
fizz_buzz(15)

# Expected output:
print("\nExpected output for n = 15:")
print("1")
print("2")
print("Fizz")  # For 3
print("4")
print("Buzz")  # For 5
print("Fizz")  # For 6
print("7")
print("8")
print("Fizz")  # For 9
print("Buzz")  # For 10
print("11")
print("Fizz")  # For 12
print("13")
print("14")
print("FizzBuzz")  # For 15
