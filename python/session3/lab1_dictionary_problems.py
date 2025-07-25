"""Dictionary Problems - Testing student capability with dictionary operations."""


def dictionary_operations(dict1, dict2):
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    # Write your solution here
    output = {}
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        new_dict = dict1.copy()
        new_dict.update(dict2)
        output['merged'] = new_dict
        dict1_keys = set(dict1.keys())
        dict2_keys = set(dict2.keys())
        output['common_keys'] = dict1_keys & dict2_keys
        output['unique_keys'] = set(new_dict.keys()) - output['common_keys']
    elif isinstance(dict1,dict):
        output['merged'] = dict1
        output['common_keys'] = dict1
        output['unique_keys'] = dict1
    elif isinstance(dict2,dict):
        output['merged'] = dict2
        output['common_keys'] = dict2
        output['unique_keys'] = dict2
    return output

def count_word_frequency(text):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    # Write your solution here
    output = {}
    if isinstance(text,str):
        words = text.split(" ")
        for word in words:
            output.setdefault(word,0)
            output[word] += 1
    return output


def dictionary_filtering(students_grades):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    # Write your solution here
    output = {}
    if isinstance(students_grades,dict):
        output = dict(filter(lambda x: x[1] >= 70,students_grades.items()))
    return output


def nested_dictionary_access(nested_dict, keys_path):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    # Write your solution here
    output = None
    if isinstance(nested_dict,dict) and isinstance(keys_path,list):
        current_pointer = nested_dict
        for key in keys_path:
            current_pointer = current_pointer.get(key,None)
            if current_pointer is None:
                break
        output = current_pointer
    return output


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
