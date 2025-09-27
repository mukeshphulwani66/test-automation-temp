def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.
    
    Args:
        arr (List[int]): Sorted list of integers to search through
        target (int): The value to search for
        
    Returns:
        int: Index of the target if found, -1 otherwise
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
# sorted_array = [1, 3, 5, 7, 9]
# print(binary_search(sorted_array, 3))  # Output: 1
# print(binary_search(sorted_array, 4))  # Output: -1