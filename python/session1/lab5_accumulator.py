"""Sum 1 … n — Compute and display the running total."""


def compute(number):
    """write your soulution Here Sum 1 … n — Compute and display the running total."""
    accu = 0
    i = 1
    while i <= number:
        accu+=i
        print(f"Running total after adding {i}: {accu}")
        i+=1
    return accu

if __name__ == "__main__":
    assert compute(5) == 15, "Test case failed"
    assert compute(10) == 55, "Test case failed"
    assert compute(100) == 5050, "Test case failed"
    assert compute(0) == 0, "Test case failed"
    assert compute(1) == 1, "Test case failed"
    assert compute(2) == 3, "Test case failed"
    assert compute(3) == 6, "Test case failed"
    assert compute(4) == 10, "Test case failed"
