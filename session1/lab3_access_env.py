""" A python program to access environment variables. TEST1234, TEST1235, TEST1236"""

import os


def access_env(env_var):
    """Access the environment variable and return its value."""
    return os.environ.get(env_var)


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
