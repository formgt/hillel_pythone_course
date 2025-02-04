import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):

    with codecs.open(html_file, "r", "utf-8") as file:
        content = file.read()

    cleaned = re.sub(r"<[^>]*>", "", content)

    cleaned_lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
    result_text = "\n".join(cleaned_lines)

    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(result_text)
