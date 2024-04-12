import main

def test_factorial():
    assert main.factorial(0) == 1
    assert main.factorial(5) == 120
    assert main.factorial(10) == 3628800


def test_fibonacci():
    assert main.fibonacci(0) == 0
    assert main.fibonacci(1) == 1
    assert main.fibonacci(5) == 5
    assert main.fibonacci(10) == 55


def test_square_root():
    assert main.square_root(9) == 3.0
    assert main.square_root(16) == 4.0


def test_power():
    assert main.power(2, 3) == 8
    assert main.power(3, 4) == 81


# Run the tests
if __name__ == "__main__":
    test_factorial()
    print("Factorial tests passed!")

    test_fibonacci()
    print("Fibonacci tests passed!")

    test_square_root()
    print("Square root tests passed!")

    test_power()
    print("Power tests passed!")
