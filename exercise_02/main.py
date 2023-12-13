import time
import random

# Define the Fibonacci sequence implementation
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Choose a random number between 15 and 35
n = random.randint(15, 35)

# Record the start time
start_time = time.time()

# Calculate the nth Fibonacci number
fib_number = fibonacci(n)

# Record the end time
end_time = time.time()

# Calculate the time taken to compute the Fibonacci number
time_taken = end_time - start_time

# Print out the result and the time taken
print(f"fib({n})={fib_number}")
print(f"took {time_taken} seconds")

