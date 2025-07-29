"""A Python program to count the number 4 in a given list."""

def count(lst):
    """Count the occurrences of the number 4 in the given list."""
    return lst.count(4) # Using the count method of list to count occurrences of 4


if __name__ == "__main__":
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"
