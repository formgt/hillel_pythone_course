input_number = int(input("Enter a 5-digit number: "))

input_number_5 = input_number % 10
input_number //= 10

input_number_4 = input_number % 10
input_number //= 10

input_number_3 = input_number % 10
input_number //= 10

input_number_2 = input_number % 10
input_number //= 10

input_number_1 = input_number % 10
input_number //= 10

reversed_number = input_number_5 * 10000 + input_number_4 * 1000 + input_number_3 * 100 + input_number_2 * 10 + input_number_1

print(reversed_number)
