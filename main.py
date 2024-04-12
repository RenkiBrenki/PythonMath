import math


# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Function to calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Function to calculate the square root of a number
def square_root(x):
    return math.sqrt(x)


# Function to calculate the power of a number
def power(base, exponent):
    return base ** exponent


# Example usage of the functions
if __name__ == "__main__":
    num = 5
    print("Factorial of", num, "is", factorial(num))

    fib_num = 7
    print("Fibonacci number at position", fib_num, "is", fibonacci(fib_num))

    square = 25
    print("Square root of", square, "is", square_root(square))

    base = 2
    exponent = 3
    print(base, "raised to the power of", exponent, "is", power(base, exponent))