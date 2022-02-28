"""
Author: Rob Homa
Program: Using Python to solve pi (kind of)
Note: This will not give you the 100% answer of pi, it is only an estimate
"""

import math
import random

# Declaring variables to be used later
inside = 0
total = 0

# Ask user for the number of operations
print("# of operations:")
operations = input()

# Main loop
while int(operations) >= 1:
    x = random.random()
    y = random.random()
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance <= 1:
        total = int(total) + 1
        inside = int(inside) + 1
    else:
        total = total + 1
    operations = int(operations) - 1

# Final calculation and output
pi = inside / total * 4
print("Pi is about " + str(pi))
