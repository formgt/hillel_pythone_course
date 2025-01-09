import re
import keyword

pattern = re.compile(r'^(?!.*__)[a-z_][a-z0-9_]*$')


def is_valid_variable(name: str) -> bool:
    if not name:
        return False
    if name in keyword.kwlist:
        return False
    return bool(pattern.match(name))


tests = [
    "_",
    "__",
    "___",
    "x",
    "get_value",
    "get value",
    "get!value",
    "some_super_puper_value",
    "Get_value",
    "get_Value",
    "getValue",
    "3m",
    "m3",
    "assert",
    "assert_exception",
]

for test_str in tests:
    print(f"{test_str} => {is_valid_variable(test_str)}")
