# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_numbers(numbers: list) -> int:
    """Returns the sum of a list of numbers."""
    return sum(numbers)

# Example usage
nums = [1, 2, 3, 4, 5]
print(f"Sum: {sum_numbers(nums)}")  # Output: Sum: 15