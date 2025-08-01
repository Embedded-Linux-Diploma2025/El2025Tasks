"""Tuple Problems - Testing student capability with tuple operations."""


def tuple_operations(tuple1: tuple, tuple2: tuple):
    """Perform basic operations on two tuples.

    Args:
        tuple1 (tuple): First tuple
        tuple2 (tuple): Second tuple

    Returns:
        dict: Dictionary with concatenation, repetition,
    """
    # Write your solution here
    list_conc=[]
    list_rep=[]
    for i in tuple1:
        list_conc.append(i)
        list_rep.append(i)

    list_rep.extend(list_rep)
    for i in tuple2:
        list_conc.append(i)
    tuple_dict={"concatenation" : tuple(list_conc),"repetition" : tuple(list_rep) }

    return tuple_dict


def find_tuple_stats(numbers_tuple :tuple):
    """Calculate statistics for a tuple of numbers.

    Args:
        numbers_tuple (tuple): Tuple of numbers

    Returns:
        tuple: (sum, max, min, length)
    """
    # Write your solution here
    tuple_sum=0
    tuple_max=numbers_tuple[0]
    tuple_min=numbers_tuple[0]
    for i in numbers_tuple:
        tuple_sum+=i
        tuple_max = max(i,tuple_max)
        tuple_min = min(i,tuple_min)
    tuple_length = len(numbers_tuple)
    return  (tuple_sum,tuple_max,tuple_min,tuple_length)


def count_elements_in_tuple(data_tuple :tuple, element : int):
    """Count occurrences of an element in a tuple.

    Args:
        data_tuple (tuple): Tuple to search in
        element: Element to count

    Returns:
        int: Number of occurrences
    """
    # Write your solution here
    return data_tuple.count(element)


def tuple_indexing_slicing(data_tuple:tuple):
    """Demonstrate tuple indexing and slicing operations.

    Args:
        data_tuple (tuple): Input tuple

    Returns:
        dict: Dictionary with various slicing results
    """
    # Write your solution here
    index_slicing_dict= {"first_element" : data_tuple[0], "last_element" : data_tuple[-1]}
    return index_slicing_dict

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
