"""
====================================================
Algorithm: Linear Search

Description:
Linear Search (or Sequential Search) is one of the simplest searching algorithms.
It goes through each element in the list sequentially until it finds the target value 
or reaches the end of the list.
 
Works on: both sorted and unsorted arrays.

Time Complexity: 
    - Best Case: O(1)
    - Average Case: O(n)
    - Worst Case: O(n)
Space Complexity: O(1)
====================================================
"""

def linear_search(arr, target):
    """
    🔍 Perform a linear search to find the index of a target value in a list.

    Args:
        arr (list): The list of elements to search through.
        target (any): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.

    Example:
        >>> linear_search([5, 3, 8, 6], 8)
        2
    """

    # Iterate through each element and check if it matches the target
    for index, element in enumerate(arr):
        # Comparison step
        if element == target:
            return index  # ✅ Target found, return its index

    # If target not found, return -1
    return -1

if __name__ == "__main__":
    # Example dataset
    data = [10, 23, 45, 70, 11, 15]
    target = 70

    print("Data:", data)
    print(f"Target value: {target}")

    result = linear_search(data, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")