 def pop_snap(n):
    result = []  # Initialize an empty list to store the results.
    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive).
        # Check divisibility and append the appropriate string.
        if i % 3 == 0 and i % 5 == 0:
            result.append("PopSnap")
        elif i % 3 == 0:
            result.append("Pop")
        elif i % 5 == 0:
            result.append("Snap")
        else:
            result.append(str(i))  # Convert the integer to a string.
    return result

# Example usage:
n = 15
print(pop_snap(n))
