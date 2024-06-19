def find_missing_element(arr):
    full_set = set(range(1, 11))
    input_set = set(arr)
    missing_element = full_set - input_set
    return list(missing_element)[0]

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 9, 10] # Replace this with your own list
missing = find_missing_element(arr)
print("The missing element is:", missing)