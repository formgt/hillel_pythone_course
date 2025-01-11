import keyword


def is_valid_variable(name: str) -> bool:
    if not name:
        return False

    if name in keyword.kwlist:
        return False

    if set(name) == {'_'}:
        return len(name) == 1

    if name[0].isdigit():
        return False

    if any(ch.isupper() for ch in name):
        return False

    if not all(ch.islower() or ch.isdigit() or ch == '_' for ch in name):
        return False

    return True


tests = [
    "",
    "_",
    "__",
    "___",
    "m3",
    "some__name",
    "3name",
    "Name",
    "a-b",
    "import",
    "__var_name",
]

for t in tests:
    print(f"{t!r:15} => {is_valid_variable(t)}")
