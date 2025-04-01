
def longest_even_odd_subarray(arr):
    """
    Finds the longest contiguous subarray with an equal number of even and odd elements.
    
    Parameters:
    arr (list): List of integers.
    
    Returns:
    list: The longest contiguous subarray with equal numbers of odd and even elements.
    """
    # Dictionary to store earliest occurrence of each prefix sum.
    prefix_sum_to_index = {}
    
    # Initialize current prefix sum, max length, and starting index.
    curr_sum = 0
    max_length = 0
    start_index = -1
    
    # Initialize with prefix sum 0 at index -1 to handle subarrays starting at index 0.
    prefix_sum_to_index[0] = -1
    
    for i, num in enumerate(arr):
        # Map the integer: even -> +1, odd -> -1.
        if num % 2 == 0:
            curr_sum += 1
        else:
            curr_sum -= 1
        
        # If this prefix sum is seen for the first time, record its index.
        if curr_sum not in prefix_sum_to_index:
            prefix_sum_to_index[curr_sum] = i
        
        # If the prefix sum has been seen before, a zero-sum subarray exists.
        if curr_sum in prefix_sum_to_index:
            prev_index = prefix_sum_to_index[curr_sum]
            subarray_length = i - prev_index
            if subarray_length > max_length:
                max_length = subarray_length
                start_index = prev_index + 1

    # No valid subarray found, return an empty list.
    if max_length == 0:
        return []
    
    return arr[start_index:start_index + max_length]

# Example usage:
if __name__ == "_main_":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]  # Example array
    result = longest_even_odd_subarray(arr)
    print("Longest subarray with equal number of even and odd elements:")
    print(result)