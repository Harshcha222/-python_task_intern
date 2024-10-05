def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    Parameters:
    str1 (str): The first string to check.
    str2 (str): The second string to check.
    
    Returns:
    bool: True if str1 and str2 are anagrams, False otherwise.
    """
    # Normalize the strings: remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort and compare the strings
    return sorted(str1) == sorted(str2)

# Example usage:
print(is_anagram("listen", "silent"))  # Should return True
print(is_anagram("hello", "world"))    # Should return False

# Add test cases
print("\nRunning Anagram Checker with 'listen' and 'silent':")
print(is_anagram("listen", "silent"))

print("\nExpected output for 'listen' and 'silent': True")
