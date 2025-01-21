def popular_words(text, words):

    text_lower = text.lower().split()
    counts = {}
    for w in text_lower:
        counts[w] = counts.get(w, 0) + 1
    return {w: counts.get(w, 0) for w in words}


def run_tests():

    text = """When I was One
              I had just begun
              When I was Two
              I was nearly new
           """
    test_words = ["i", "was", "three", "near"]
    expected = {"i": 4, "was": 3, "three": 0, "near": 0}

    result = popular_words(text, test_words)

    print("Result  :", result)
    print("Expected:", expected)
    assert result == expected, "Test FAILED"
    print("OK")


if __name__ == "__main__":
    run_tests()
