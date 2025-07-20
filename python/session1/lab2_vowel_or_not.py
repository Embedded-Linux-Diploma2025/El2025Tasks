"""Write a Python program to test whether a passed letter is a vowel or not."""


def vowel(letter):
    """Write your solution here. Don't forget to return the result at the end."""
    vowel_letters = ('a', 'e', 'o', 'u', 'i')
    result: bool = False
    if letter.lower() in vowel_letters:
        print("letter " + letter + " is vowel")
        result = True
    elif letter.lower() not in vowel_letters:
        print("letter " + letter + " is not vowel")
        result = False
    elif not letter.isalpha():
        print("please enter a valid letter")
        result =  None
    else:
        print("something wrong try again")
    return result

if __name__ == "__main__":
    assert vowel("a"), "Test case failed"
    assert not vowel("b"), "Test case failed"
    assert vowel("A"), "Test case failed"
    assert not vowel("B"), "Test case failed"
    assert vowel("e"), "Test case failed"
    assert vowel("E"), "Test case failed"
    assert vowel("i"), "Test case failed"
    assert vowel("I"), "Test case failed"
    assert vowel("o"), "Test case failed"
    assert vowel("O"), "Test case failed"
    assert vowel("u"), "Test case failed"
    assert vowel("U"), "Test case failed"
    assert not vowel("z"), "Test case failed"
    assert not vowel("Z"), "Test case failed"
