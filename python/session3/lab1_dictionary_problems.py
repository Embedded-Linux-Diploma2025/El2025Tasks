#!/usr/bin/python3
"""Dictionary Problems - Testing student capability with dictionary operations."""


def dictionary_operations(dict1: dict, dict2: dict):
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    # Write your solution here
    s_1=set(dict1.keys())
    s_2=set(dict2.keys())
    set_common=s_1.intersection(s_2)
    set_diff=set(dict1.keys()).symmetric_difference(dict2.keys())
    dict_merg=dict1
    dict_merg.update(dict2)
    return {"merged":dict_merg,"common_keys":set_common,"unique_keys":set_diff}


def count_word_frequency(text: str):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    # Write your solution here
    words_list=text.split(' ')
    words_set=set(words_list)
    word_freq={}
    for i in words_set:
        dict_word={i:words_list.count(i)}
        word_freq.update(dict_word)
    return word_freq


def dictionary_filtering(students_grades: dict):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    # Write your solution here
    hi_mark_students={}
    for i in students_grades:
        if students_grades[i] >= 70 :
            hi_mark_students.update({i:students_grades[i]})
    return hi_mark_students


def nested_dictionary_access(nested_dict, keys_path):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    # Write your solution here
    trgt_value=nested_dict
    for i in keys_path:
        trgt_value=trgt_value.get(i)
    return trgt_value


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
