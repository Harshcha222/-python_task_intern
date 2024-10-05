def longest_unique_substring(s):
    seen = {}  # HashMap to store characters and their indices
    start = 0
    max_len = 0
    
    for i in range(len(s)):
        if s[i] in seen and seen[s[i]] >= start:
            start = seen[s[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        
        seen[s[i]] = i  # Store the latest index of the character
    
    return max_len

# Example usage
input_string = "abcabcbb"
print("Input String:", input_string)

length_of_longest_unique_substring = longest_unique_substring(input_string)
print("Length of Longest Substring Without Repeating Characters:", length_of_longest_unique_substring)
