def merge_sort(array):
    """Sorts an array using the merge sort algorithm."""

    if len(array) <= 1:
        return array  # Base case: array of size 1 or less is already sorted

    middle = len(array) // 2
    left = merge_sort(array[:middle])  # Recursively sort the left subarray
    right = merge_sort(array[middle:])  # Recursively sort the right subarray

    return merge(left, right)  # Merge the sorted subarrays


def merge(left, right):
    """Merges two sorted arrays into a single sorted array."""

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]  # Append any remaining elements from the left subarray
    result += right[j:]  # Append any remaining elements from the right subarray

    return result

# Example usage:
array = [5, 2, 4, 7, 1, 3, 6]
sorted_array = merge_sort(array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5, 6, 7]
