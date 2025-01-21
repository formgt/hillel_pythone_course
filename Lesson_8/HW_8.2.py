def is_palindrome(text: str) -> bool:
    filtered_text = ''.join(ch.lower() for ch in text if ch.isalnum())
    n = len(filtered_text)
    for i in range(n // 2):
        if filtered_text[i] != filtered_text[n - 1 - i]:
            return False
    return True

assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("0P") is False
assert is_palindrome("a.") is True
assert is_palindrome("aurora") is False
print("OK")
