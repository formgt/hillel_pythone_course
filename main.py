input_number = int(input('Enter a 4-digit number: '))
input_number_1 = input_number // 1000
input_number_2 = (input_number // 100) % 10
input_number_3 = (input_number // 10) % 10
input_number_4 = input_number % 10
print(input_number_1)
print(input_number_2)
print(input_number_3)
print(input_number_4)
