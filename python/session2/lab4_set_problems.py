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
    operations_dict = {}
    if isinstance(set1,set) and isinstance(set2,set):
        operations_dict["union"] = set1 | set2
        operations_dict["intersection"] = set1 & set2
        operations_dict["difference"] = operations_dict["union"] - operations_dict["intersection"]
    elif isinstance(set1,set):
        operations_dict["union"] = set1
        operations_dict["intersection"] = set1
        operations_dict["difference"] = set1
    elif isinstance(set1,set):
        operations_dict["union"] = set2
        operations_dict["intersection"] = set2
        operations_dict["difference"] = set2
    return operations_dict

def find_unique_elements(list1, list2):
    """Find elements that are unique to each list using sets.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        tuple: (unique_to_list1, unique_to_list2)
    """
    # Write your solution here
    operations_tuple = tuple()
    if isinstance(list1,list) and isinstance(list2,list):
        set1 = set(list1)
        set2 = set(list2)
        diff1 = set1 - set2
        diff2 = set2 - set1
        operations_tuple = tuple([diff1,diff2])
    elif isinstance(list1,list):
        operations_tuple = tuple([set(list1),set(list1)])
    elif isinstance(list2,list):
        operations_tuple = tuple([set(list2),set(list2)])
    return operations_tuple


def remove_vowels_set(text):
    """Remove vowels from text using set operations.

    Args:
        text (str): Input text

    Returns:
        str: Text with vowels removed
    """
    # Write your solution here
    vowels = set(['a','A','e','E','o','O','u','U','i','I'])
    new_str = ""
    if isinstance(text,str):
        text_set = set(text)
        text_set.difference_update(vowels)
        new_str = str(text_set)
    return new_str


if __name__ == "__main__":
    # Test cases
    print("Testing set_operations...")
    result = set_operations({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result["union"] == {1, 2, 3, 4, 5, 6}, "Union test failed"
    assert result["intersection"] == {3, 4}, "Intersection test failed"
    assert result["difference"] == {1,2,5,6}, "difference test failed"

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
