import math
import random
import statistics
import keyword

x = math.pow(2, 3)
print(x)

x = random.randint(0, 100)
print(x)

# mean
nums = [1, 5, 33, 12, 46, 33, 2]
z = statistics.mean(nums)
print(z)

# median
z = statistics.median(nums)
print(z)

# mode
z = statistics.mode(nums)
print(z)

y = keyword.iskeyword("for")
print(y)

y = keyword.iskeyword("football")
print(y)
