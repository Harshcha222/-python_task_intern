def find_missing(nums, n):
    """
    Finds the missing number in the list of n-1 integers from the range 1 to n.
    
    Parameters:
    nums (list): List of n-1 integers from the range 1 to n.
    n (int): The range from 1 to n.
    
    Returns:
    int: The missing number in the list.
    """
    # Sum of first n natural numbers
    total_sum = n * (n + 1) // 2
    
    # Sum of the numbers in the given list
    current_sum = 0
    for i in nums:
        current_sum += i
    
    # The missing number is the difference between the total sum and the current sum
    return total_sum - current_sum

# Test cases
print(find_missing([1, 2, 3, 5], 5))  # Expected output: 4
print(find_missing([1, 2, 4, 5], 5))  # Expected output: 3
print(find_missing([2, 3, 4, 5], 5))  # Expected output: 1
print(find_missing([1, 3, 4, 5], 5))  # Expected output: 2
