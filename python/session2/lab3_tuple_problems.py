"""Tuple Problems - Testing student capability with tuple operations."""


def tuple_operations(tuple1, tuple2):
    """Perform basic operations on two tuples.

    Args:
        tuple1 (tuple): First tuple
        tuple2 (tuple): Second tuple

    Returns:
        dict: Dictionary with concatenation, repetition,
    """
    conc_tuple = tuple1 + tuple2
    rep_tuple = tuple1 * 2
    dict_result = {
        "concatenation": conc_tuple,
        "repetition": rep_tuple
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
    tsum = sum(numbers_tuple)
    tmax = max(numbers_tuple)
    tmin = min(numbers_tuple)
    tlen = len(numbers_tuple)

    res_tuple = (tsum, tmax, tmin, tlen)

    return res_tuple


def count_elements_in_tuple(data_tuple, element):
    """Count occurrences of an element in a tuple.

    Args:
        data_tuple (tuple): Tuple to search in
        element: Element to count

    Returns:
        int: Number of occurrences
    """
    result = data_tuple.count(element)
    return result


def tuple_indexing_slicing(data_tuple):
    """Demonstrate tuple indexing and slicing operations.

    Args:
        data_tuple (tuple): Input tuple

    Returns:
        dict: Dictionary with various slicing results
    """
    # Write your solution here
    first_element = data_tuple[0]
    last_element = data_tuple[-1]

    dict_result = {
        "first_element": first_element,
        "last_element": last_element
    }
    return dict_result

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
