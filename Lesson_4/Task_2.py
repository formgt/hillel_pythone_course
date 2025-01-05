lst = [0, 1, 7, 2, 4, 8]
#lst = [1, 3, 5]
#lst = [6]
#lst = []

sum_even_index = 0
for i in range(len(lst)):
    if i % 2 == 0:
        sum_even_index += lst[i]

if len(lst) == 0:
    result = 0
else:
    result = sum_even_index * lst[-1]

print(result)
