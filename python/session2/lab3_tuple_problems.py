"""Tuple Problems - Testing student capability with tuple operations."""


def tuple_operations(tuple1, tuple2):
    """Perform basic operations on two tuples.

    Args:
        tuple1 (tuple): First tuple
        tuple2 (tuple): Second tuple

    Returns:
        dict: Dictionary with concatenation, repetition,
    """
    # Write your solution here
    dict_conc: tuple = tuple1 + tuple2
    # print(dict_conc)
    dict_rep = tuple1 * 2
    # print(dict_rep)
    dict_result = {
        "concatenation": dict_conc,
        "repetition": dict_rep
    }
    return dict_result


def find_tuple_stats(numbers_tuple):
    """Calculate statistics for a tuple of numbers.

    Args:
        numbers_tuple (tuple): Tuple of numbers

    Returns:
        tuple: (sum, max, min, length)
    """
    # Write your solution here
    # print(type(numbers_tuple))
    # print(numbers_tuple)
    # calc sum
    tuple_sum = 0
    for num in numbers_tuple:
        tuple_sum+=num
    # print(tuple_sum) #test
    # calc: max and min, sort the tuple
    sorted_tuple = sorted(numbers_tuple)
    # print(sorted_tuple)
    # calc: max
    tuple_max: int = sorted_tuple[-1]
    # print(sorted_tuple[-1])
    # calc: min
    tuple_min: int = sorted_tuple[0]
    # print(sorted_tuple[0])
    # calc: lenght
    tuple_length: int = len(numbers_tuple)
    # print(tuple_length)
    tuple_result = (tuple_sum, tuple_max, tuple_min, tuple_length)
    return tuple_result


def count_elements_in_tuple(data_tuple, element):
    """Count occurrences of an element in a tuple.

    Args:
        data_tuple (tuple): Tuple to search in
        element: Element to count

    Returns:
        int: Number of occurrences
    """
    # Write your solution here
    # result = data_tuple.count(element)
    return data_tuple.count(element)

def tuple_indexing_slicing(data_tuple):
    """      tuple indexing and slicing operations.

    Args:
        data_tuple (tuple): Input tuple

    Returns:
        dict: Dictionary with various slicing results
    """
    # Write your solution here
    first = data_tuple[0]
    last = data_tuple[-1]
    tuple_reversed = data_tuple[::-1]
    data_result = {
            "first_element": first,          # first item
            "last_element": last,            # last item
            "reversed": tuple_reversed             # reversed tuple
        }
    return data_result

if __name__ == "__main__":
    # Test cases
    print("Testing tuple_operations...")
    result = tuple_operations((1, 2, 3), (3, 4, 5))
    expected_keys = {"concatenation", "repetition"}
    expected = {"concatenation": (1, 2, 3, 3, 4, 5), "repetition": (1, 2, 3, 1, 2, 3)}
    assert result == expected, f"Expected {expected}, got {result}"
    assert result["concatenation"] == (1, 2, 3, 3, 4, 5), (
        f"Expected concatenation (1, 2, 3, 3, 4, 5), got {result['concatenation']}"
    )
    assert result["repetition"] == (1, 2, 3, 1, 2, 3), "Expected repetition (1, 2, 3, 1, 2, 3)"
    assert set(result.keys()) == expected_keys, f"Expected keys {expected_keys}"

    print("Testing find_tuple_stats...")
    result = find_tuple_stats((1, 5, 3, 9, 2))
    assert result == (20, 9, 1, 5), f"Expected (20, 9, 1, 5), got {result}"

    print("Testing count_elements_in_tuple...")
    result = count_elements_in_tuple((1, 2, 3, 2, 4, 2), 2)
    assert result == 3, f"Expected 3, got {result}"

    print("Testing tuple_indexing_slicing...")
    result = tuple_indexing_slicing((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    assert "first_element" in result, "Should contain first_element"
    assert "last_element" in result, "Should contain last_element"
    assert result["first_element"] == 0, f"Expected first_element 0, got {result['first_element']}"
    assert result["last_element"] == 9, f"Expected last_element 9, got {result['last_element']}"

    print("All tests passed!")
