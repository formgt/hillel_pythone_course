list_1 = [1, 2, 3, 4, 5, 6]
# list_1 = [1, 2, 3]
# list_1 = [1, 2, 3, 4, 5]
# list_1 = [1]
# list_1 = []

middle_index = (len(list_1) + 1) // 2

first_half = list_1[:middle_index]
second_half = list_1[middle_index:]
result_list = [first_half, second_half]
print(result_list)
