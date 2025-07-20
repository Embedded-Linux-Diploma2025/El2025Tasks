"""Dictionary Problems - Testing student capability with dictionary operations."""

def dictionary_operations(dict1:dict, dict2:dict)->dict:
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    # Write your solution here
    mer = dict1 | dict2
    comm_k= set(dict1).intersection(dict2)
    uni_k1=set(dict1).difference(dict2)
    uni_k2=set(dict2).difference(dict1)
    uni_k= set(uni_k1).union(uni_k2)
    dicti = {"merged": mer, "common_keys": comm_k , "unique_keys": uni_k}
    return dicti


def count_word_frequency(text:str):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    # Write your solution here
    words= text.split()
    counter={}
    for i in words:
        counter[i] = counter.get(i,0)+1
    return counter


def dictionary_filtering(students_grades:dict):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    # Write your solution
    overseventy={}
    for grade in students_grades:
        if students_grades[grade] >= 70 :
            overseventy[grade]= students_grades[grade]
    return overseventy



def nested_dictionary_access(nested_dict:dict, keys_path):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    # Write your solution here
    current=nested_dict
    for key in keys_path:
        if isinstance(current,dict) and key in current:
            current=current[key]
        else:
            return None
    return current


result = dictionary_operations({"a": 1, "b": 2} , {"b": 3, "c": 4})
print(result)
result = count_word_frequency("hello world hello python world")
print(result)
result = dictionary_filtering({"Alice": 85, "Bob": 65, "Charlie": 90, "Diana": 45})
print(result)
nested = {"level1": {"level2": {"level3": "found"}}}
result = nested_dictionary_access(nested, ["level1", "level2", "level3"])
print(result)


if __name__ == "__main__":
    # Test cases
    print("Testing dictionary_operations...")
    result = dictionary_operations({"a": 1, "b": 2}, {"b": 3, "c": 4})
    expected = {"merged": {"a": 1, "b": 3, "c": 4}, "common_keys": {"b"}, "unique_keys": {"a", "c"}}
    assert result == expected, f"Expected {expected}, got {result}"
    assert result["merged"] == {"a": 1, "b": 3, "c": 4}, "Merged dictionary incorrect"
    assert result["common_keys"] == {"b"}, "Common keys incorrect"
    assert result["unique_keys"] == {"a", "c"}, "Unique keys incorrect"

    print("Testing count_word_frequency...")
    result = count_word_frequency("hello world hello python world")
    expected = {"hello": 2, "world": 2, "python": 1}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing dictionary_filtering...")
    result = dictionary_filtering({"Alice": 85, "Bob": 65, "Charlie": 90, "Diana": 45})
    expected = {"Alice": 85, "Charlie": 90}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing nested_dictionary_access...")
    nested = {"level1": {"level2": {"level3": "found"}}}
    result = nested_dictionary_access(nested, ["level1", "level2", "level3"])
    assert result == "found", f"Expected 'found', got {result}"

    result = nested_dictionary_access(nested, ["level1", "nonexistent"])
    assert result is None, f"Expected None, got {result}"

    print("All tests passed!")
