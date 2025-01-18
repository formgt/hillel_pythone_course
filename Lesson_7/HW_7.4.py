def common_elements():
    set_multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    set_multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    return set_multiples_of_3 & set_multiples_of_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, "Test 1"
print("OK")
