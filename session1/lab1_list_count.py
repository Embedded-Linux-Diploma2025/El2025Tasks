"""Write a Python program to count the number 4 in a given list."""


def count(lst):
    """Write your solution here. Don't forget to return the result at the end."""
    count_of_4=0
    for idx , val in enumerate(lst):
        print(idx)
        if val==4:
            count_of_4+=1
    print("Total Count is : ", {count_of_4})
    print("End of count()")
    return count_of_4


if __name__ == "__main__":
    # Test cases
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"
