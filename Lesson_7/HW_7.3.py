def find_second_index(source_text: str, substring: str) -> int or None:
    first_index = source_text.find(substring)
    if first_index == -1:
        return None

    second_index = source_text.find(substring, first_index + 1)
    if second_index == -1:
        return None

    return second_index


assert find_second_index("sims", "s") == 3, "Test1"
assert find_second_index("find the river", "e") == 12, "Test2"
assert find_second_index("hi", "h") is None, "Test3"
assert find_second_index("Hello, hello", "lo") == 10, "Test4"
assert find_second_index("Hello, hello, hello", "lo") == 10, "Test5"
assert find_second_index("Heee", "e") == 2, "Test6"
assert find_second_index("Hello, hello", "poo") is None, "Test7"

print("OK.")
