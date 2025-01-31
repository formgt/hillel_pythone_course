import string


def get_first_word(text_str):
    for punctuation_mark in string.punctuation:
        if punctuation_mark != "'":
            text_str = text_str.replace(punctuation_mark, " ")
    splitted_words = text_str.split()
    return splitted_words[0] if splitted_words else ""


assert get_first_word("Hello world") == "Hello", "Test1"
assert get_first_word("greetings, friends") == "greetings", "Test2"
assert get_first_word("don't touch it") == "don't", "Test3"
assert get_first_word(".., and so on ...") == "and", "Test4"
assert get_first_word("hi") == "hi", "Test5"
assert get_first_word("Hello.World") == "Hello", "Test6"
print("OK")
