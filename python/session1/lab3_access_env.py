"""Write a python program to access environment variables. TEST1234, TEST1235, TEST1236"""

import os


def access_env(env_var):
    """Write your solution here. Don't forget to return the result at the end."""
    # return the value of the passed environment variable
    # print("enviVariable: ", env_var,  "value: " , os.environ[env_var])
    return os.environ[env_var]

if __name__ == "__main__":
    os.environ["TEST1234"] = "test_value"
    os.environ["TEST1235"] = "test_value2"
    os.environ["TEST1236"] = "test_value3"
    assert access_env("TEST1234") == "test_value"
    assert access_env("TEST1235") == "test_value2"
    assert access_env("TEST1236") == "test_value3"
    assert access_env("TEST1234") == "test_value"
    assert access_env("TEST1235") == "test_value2"
    assert access_env("TEST1236") == "test_value3"
