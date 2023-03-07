import time
import math

# Prompt user for input values
val = int(input("Enter a value to find the square root of: "))
delay = int(
    input("Enter the number of milliseconds to wait before computing the square root: ")
)

# Convert delay to seconds
delay = delay / 1000.0

# Wait for specified amount of time
time.sleep(delay)

# Compute square root
sqrt_val = math.sqrt(val)

# Print result
print("Square root of", val, "after", delay * 1000, "milliseconds is", sqrt_val)
