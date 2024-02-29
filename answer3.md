def flatten_array(arr):
    result = []  # Initialize the result list.
    for item in arr:
        if isinstance(item, list):  # If the item is a list, recurse.
            result.extend(flatten_array(item))  # Extend the result list with the flattened list.
        else:
            result.append(item)  # If the item is a number, append it to the result list.
    return result

# Example usage:
arr = [1, [2, 3], [[4], [5]]]
print(flatten_array(arr))