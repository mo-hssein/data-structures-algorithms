import unittest


def fibonacci_dp(n):
    """
    Calculates the Fibonacci number using dynamic programming.
    Time complexity = O(n)

    Parameters:
    - n (int): The position in the Fibonacci sequence to calculate.

    Returns:
    - fib[n] (int): The Fibonacci number at the n-th position.
    """
    # If n is 0, return 0 directly
    if n == 0:
        return 0

    # Initialize an array to store Fibonacci sequence values up to n
    fib = [0] * (n + 1)
    fib[1] = 1  # Set the second value in the sequence to 1

    # Compute the rest of the Fibonacci sequence values
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    # Return the n-th Fibonacci number
    return fib[n]


# unit testing

#      |
#      |
#      V

class TestFibonacciDP(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci_dp(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci_dp(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci_dp(2), 1)

    def test_fibonacci_3(self):
        self.assertEqual(fibonacci_dp(3), 2)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci_dp(4), 3)

    def test_fibonacci_5(self):
        self.assertEqual(fibonacci_dp(5), 5)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci_dp(10), 55)

    def test_large_fibonacci(self):
        self.assertEqual(fibonacci_dp(50), 12586269025)


if __name__ == "__main__":
    unittest.main()
