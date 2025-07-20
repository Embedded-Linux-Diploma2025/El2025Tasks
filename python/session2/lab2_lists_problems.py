"""List Problems - Testing student capability with list operations."""


def find_max_min(numbers):
    """Find the maximum and minimum values in a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        tuple: (max_value, min_value)
    """
    # Write your solution here
    # solution like c
    # max_elem = numbers[0]
    # min_elem = numbers[0]
    # for element in numbers:
    #     if element > max_elem:
    #         max_elem = element
    #     elif element < min_elem:
    #         min_elem = element
    # solution 2
    max_elem = max(numbers)
    min_elem = min(numbers)
    ret = (max_elem, min_elem)
    return ret

def reverse_list(items):
    """Reverse a list without using built-in reverse() method.

    Args:
        items (list): List to reverse

    Returns:
        list: Reversed list
    """
    # Write your solution here
    reversed_list = []
    for element in range(len(items), 0, -1):
        reversed_list.append(element)
    return reversed_list

def list_statistics(numbers):
    """Calculate basic statistics for a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        dict: Dictionary with sum, average, count
    """
    # Write your solution here
    list_sum = sum(numbers)
    list_length = len(numbers)
    list_average = list_sum / list_length
    ret_dic = {"sum":list_sum, "average":list_average, "count": list_length}
    return ret_dic

def flatten_nested_list(nested_list):
    """Flatten a nested list structure.

    Args:
        nested_list (list): List containing sublists

    Returns:
        list: Flattened list
    """
    # Write your solution here
    new_list = []
    for element in nested_list:
        if isinstance(element, int):
            new_list.append(element)
        else:
            new_list.extend(flatten_nested_list(element))
    return new_list

if __name__ == "__main__":
    # Test cases
    print("Testing find_max_min...")
    result = find_max_min([1, 5, 3, 9, 2])
    assert result == (9, 1), f"Expected (9, 1), got {result}"

    print("Testing reverse_list...")
    result = reverse_list([1, 2, 3, 4, 5])
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], got {result}"

    print("Testing list_statistics...")
    result = list_statistics([1, 2, 3, 4, 5])
    expected = {"sum": 15, "average": 3.0, "count": 5}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing flatten_nested_list...")
    result = flatten_nested_list([[1, 2], [3, 4], [5, 6]])
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], got {result}"

    print("All tests passed!")
