"""
====================================================
Algorithm: Binary Search

Description:
Binary Search is an efficient algorithm used to find the position of a target 
value within a sorted array. It works by repeatedly dividing the search interval 
in half, comparing the middle element with the target value.

If the target matches the middle element, the search ends.
If the target is smaller, the search continues in the left half.
If the target is larger, the search continues in the right half.

Works on: sorted arrays only.

Time Complexity:
    - Best Case: O(1)
    - Average Case: O(log n)
    - Worst Case: O(log n)
Space Complexity: O(1)
====================================================
"""

def binary_search(arr, target):
    """
    🔍 Perform a binary search to find the index of a target value in a sorted list.

    Args:
        arr (list): The sorted list of elements to search through.
        target (any): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.

    Example:
        >>> binary_search([1, 3, 5, 7, 9], 5)
        2
    """

    left, right = 0, len(arr) - 1

    # Keep dividing the search range in half until found or range is empty
    while left <= right:
        mid = (left + right) // 2  # middle index
        mid_value = arr[mid]

        # Comparison step
        if mid_value == target:
            return mid  # Found target
        elif mid_value < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    # Target not found
    return -1


if __name__ == "__main__":
    # Example dataset (must be sorted!)
    data = [10, 20, 23, 30, 35, 40, 47, 59, 62, 70, 71, 81, 90, 95]
    target = 40

    print("Data (sorted):", data)
    print(f"Target value: {target}")

    result = binary_search(data, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")
