def infinite_fibonacci():
    """A generator that yields Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        # Update a and b: a becomes the old b, b becomes the sum
        a, b = b, a + b

# Usage:
fib_gen = infinite_fibonacci()

# To get the first 10 numbers from the infinite series:
print("First 10 Fibonacci numbers:")
for _ in range(10):
    print(next(fib_gen), end=" ")