import numpy as np
a = np.array([1, 2, 3])

print(type(a))

b = np.array([[1.5, 2-1j, 3], [4, 5, 6]], dtype=np.complex)

print(b[0][1])
print(b)
print("=========")

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)     # 1
random_number = random.choice(numbers)
print(random_number)

print("=========")

import math

print(math.sin(math.radians(30)))

print(math.sqrt(9)) 

