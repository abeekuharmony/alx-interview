#!/usr/bin/python3

"""
min_operations.py - A method to calculate the fewest number of operations needed to result in exactly n H characters.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""

def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    clipboard = 1
    h_count = 1

    while h_count < n:
        if n % h_count == 0:
            clipboard = h_count
        h_count += clipboard
        operations += 1

    if h_count == n:
        return operations

    return 0


if __name__ == "__main__":
    n = 9
    result = minOperations(n)
    print(f"Number of operations: {result}")

