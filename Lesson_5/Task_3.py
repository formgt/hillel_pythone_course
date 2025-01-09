import string


def create_hashtag(text):
    for p in string.punctuation:
        text = text.replace(p, "")
    words = text.split()
    words = [w.capitalize() for w in words]
    hashtag = "#" + "".join(words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    return hashtag


examples = [
    "Python Community",
    "i like python community!",
    "Should, I. subscribe? Yes!",
]

for ex in examples:
    print(ex, "->", create_hashtag(ex))
