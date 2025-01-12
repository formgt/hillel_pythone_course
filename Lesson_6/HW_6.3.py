def multiply_digits_until_single(num: int) -> int:
    if num < 10:
        return num

    while num > 9:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product

    return num


if __name__ == "__main__":
    user_input = input("Please enter a number: ")
    number = int(user_input)

    result = multiply_digits_until_single(number)
    print(result)
