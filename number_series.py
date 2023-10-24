def fibonacci(n):
    if n <= 0:
        return []

    # Initialize the list to store the Fibonacci sequence
    fib_sequence = [0]

    # Base case: The first two Fibonacci numbers are 0 and 1
    if n == 1:
        return fib_sequence

    fib_sequence.append(1)

    # Calculate the Fibonacci sequence for n >= 2
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

# Example usage:
n = 10  # Change this to the desired number of Fibonacci numbers
result = fibonacci(n)
print("Fibonacci Sequence (first", n, "numbers):", result)
