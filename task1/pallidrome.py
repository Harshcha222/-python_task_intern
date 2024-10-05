def is_palindrome(s):
    """
    Checks if the given string s is a palindrome.
    A palindrome reads the same forwards and backwards.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if s is a palindrome, False otherwise.
    """
    # Normalize the string: remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
test_string = "A man a plan a canal Panama"
print(f'Is the string "{test_string}" a palindrome? {is_palindrome(test_string)}')

# Test cases
print("\nRunning Palindrome Checker:")
print(f'Is "racecar" a palindrome? {is_palindrome("racecar")}')
print(f'Is "hello" a palindrome? {is_palindrome("hello")}')
print(f'Is "Madam" a palindrome? {is_palindrome("Madam")}')
print(f'Is "12321" a palindrome? {is_palindrome("12321")}')
