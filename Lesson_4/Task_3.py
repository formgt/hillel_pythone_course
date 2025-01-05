import random

n = random.randint(3, 10)

original_list = []
for _ in range(n):
    original_list.append(random.randint(0, 100))

print("Original list:", original_list)

new_list = [original_list[0], original_list[2], original_list[-2]]

print("New list:", new_list)
