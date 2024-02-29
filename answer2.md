def sum_integers_from_file(filename):
    total_sum = 0  # Initialize the sum of integers.
    with open(filename, 'r') as file:  # Open the file in read mode.
        for line in file:  # Iterate through each line in the file.
            total_sum += int(line.strip())  # Convert line to integer and add to total_sum.
    return total_sum

# Example usage:
filename = 'numbers.txt'
print(sum_integers_from_file(filename))