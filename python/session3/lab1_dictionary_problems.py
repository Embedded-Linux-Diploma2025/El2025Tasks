"""Dictionary Problems - Testing student capability with dictionary operations."""


def dictionary_operations(dict1 : dict, dict2: dict):
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    loc_dict = {"merged" : {**dict1 , **dict2}, "common_keys": {*dict2.keys()}.intersection({*dict1.keys()}), "unique_keys": {*dict1.keys()}.symmetric_difference({*dict2.keys()})}
    return loc_dict


def count_word_frequency(text :str):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    # Write your solution here
    freq_dict={}
    count=0
    for word in text.split():
        # print(freq_dict.get(word))

        if freq_dict.get(word) is not None:
            count=freq_dict.get(word)
            freq_dict[word]=count+1
        else:
            freq_dict[word]=1
        # print(word)
        # print(count)
    return freq_dict


def dictionary_filtering(students_grades : dict):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    # Write your solution here
    loop=students_grades.keys()
    top_grade={}
    for students in loop:
        if students_grades.get(students) >= 70:
            top_grade|= {students:students_grades.get(students)}
    # print(top_grade)
    return top_grade

def nested_dictionary_access(nested_dict:dict, keys_path:list):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    # Write your solution here
    for k in keys_path:
        if nested_dict.get(k) is not None:
            if isinstance(nested_dict.get(keys_path[0]), dict):
                # print(nested_dict.get(keys_path[0]))
                # print(keys_path[1:])
                return nested_dictionary_access(nested_dict.get(keys_path[0]),keys_path[1:])
                # print(nested_dict.get(keys_path[0]))
            return nested_dict.get(keys_path[0])
        return None


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
