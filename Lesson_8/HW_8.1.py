def add_one(digits):

    num = int("".join(str(d) for d in digits)) + 1
    return [int(x) for x in str(num)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("OK")
