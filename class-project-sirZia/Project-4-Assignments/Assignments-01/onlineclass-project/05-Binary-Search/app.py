def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the target value.

    :param arr: List of elements (must be sorted in ascending order).
    :param target: The value to search for.
    :return: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is at the mid index
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1

    # Target was not found in the array
    return -1

# Example usage
if __name__ == "__main__":
    # Sorted list
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    # Perform binary search
    result = binary_search(arr, target)

    # Output the result
    if result != -1:
        print(f"Element {target} is present at index {result}.")
    else:
        print(f"Element {target} is not present in the array.")