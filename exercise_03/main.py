import numpy as np

# Create a numpy list of 10 random floats ranging from 0 to 1
random_floats = np.random.rand(10)

# Calculate the mean, median, and standard deviation
mean = np.mean(random_floats)
median = np.median(random_floats)
std_dev = np.std(random_floats)

print("Random numbers:")
print(random_floats)
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
