import random

a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 15)

result = [x for x in set(a) if x in b]
print("List A:", a)
print("List B:", b)
print("Common elements:", result)
