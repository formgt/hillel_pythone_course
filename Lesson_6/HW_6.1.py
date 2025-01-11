import string


def main():
    user_input = input("Enter two letters separated by a hyphen (x-y):")
    start_char, end_char = user_input.split('-')
    all_letters = string.ascii_letters
    start_index = all_letters.index(start_char)
    end_index = all_letters.index(end_char)
    result = all_letters[start_index: end_index + 1]
    print(result)
if __name__== "__main__":
    main()