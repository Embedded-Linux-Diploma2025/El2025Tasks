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
    output = {}
    if isinstance(tuple1,tuple) and isinstance(tuple2,tuple):
        output['concatenation'] = tuple1 + tuple2
        output['repetition'] = tuple1 *2
    elif isinstance(tuple1,tuple):
        output['concatenation'] = tuple1
        output['repetition'] = tuple1
    elif isinstance(tuple2,tuple):
        output['concatenation'] = tuple2
        output['repetition'] = tuple2
    return output


def find_tuple_stats(numbers_tuple):
    """Calculate statistics for a tuple of numbers.

    Args:
        numbers_tuple (tuple): Tuple of numbers

    Returns:
        tuple: (sum, max, min, length)
    """
    # Write your solution here
    output = tuple()
    if isinstance(numbers_tuple,tuple):
        total_sum = sum(numbers_tuple)
        max_num = max(numbers_tuple)
        min_num = min(numbers_tuple)
        tuple_len = len(numbers_tuple)
        output = tuple([total_sum,max_num,min_num,tuple_len])
    return output


def count_elements_in_tuple(data_tuple, element):
    """Count occurrences of an element in a tuple.

    Args:
        data_tuple (tuple): Tuple to search in
        element: Element to count

    Returns:
        int: Number of occurrences
    """
    # Write your solution here
    num_of_occurances = 0
    if isinstance(data_tuple,tuple) and element is not None:
        num_of_occurances = data_tuple.count(element)
    return num_of_occurances


def tuple_indexing_slicing(data_tuple):
    """Demonstrate tuple indexing and slicing operations.

    Args:
        data_tuple (tuple): Input tuple

    Returns:
        dict: Dictionary with various slicing results
    """
    # Write your solution here
    output = {}
    if isinstance(data_tuple,tuple) and len(data_tuple) > 0:
        output['first_element'] = data_tuple[0]
        output['last_element'] = data_tuple[-1]
    return output


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
