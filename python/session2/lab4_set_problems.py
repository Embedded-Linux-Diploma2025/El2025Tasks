"""Set Problems - Testing student capability with set operations."""


def set_operations(set1: set, set2: set):
    """Perform basic set operations on two sets.

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        dict: Dictionary with union, intersection, difference
    """
    # Write your solution here
    return {
        "union": set1 | set2,
        "intersection": set1 & set2,
        "difference": set1 - set2,
    }


def find_unique_elements(list1, list2):
    """Find elements that are unique to each list using sets.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        tuple: (unique_to_list1, unique_to_list2)
    """
    # Write your solution here
    set1 = set(list1)
    set2 = set(list2)
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    return (unique_to_list1, unique_to_list2)


def remove_vowels_set(text):
    """Remove vowels from text using set operations.

    Args:
        text (str): Input text

    Returns:
        str: Text with vowels removed
    """
    # Write your solution here
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    # Test cases
    print("Testing set_operations...")
    result = set_operations({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result["union"] == {1, 2, 3, 4, 5, 6}, "Union test failed"
    assert result["intersection"] == {3, 4}, "Intersection test failed"

    print("Testing find_unique_elements...")
    result = find_unique_elements([1, 2, 3, 4], [3, 4, 5, 6])
    assert result[0] == {1, 2}, f"Expected {{1, 2}}, got {result[0]}"
    assert result[1] == {5, 6}, f"Expected {{5, 6}}, got {result[1]}"

    print("Testing remove_vowels_set...")
    RESULT = remove_vowels_set("Hello World")
    assert "a" not in RESULT.lower(), "Vowels should be removed"
    assert "H" in RESULT and "l" in RESULT, "Consonants should remain"

    print("Testing find_common_friends...")
    friends = {
        "Alice": {"Bob", "Charlie", "David"},
        "Bob": {"Alice", "Charlie", "Eve"},
        "Charlie": {"Alice", "Bob", "Frank"},
    }

    print("All tests passed!")
