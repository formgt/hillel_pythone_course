def get_day_word(days: int) -> str:
    last_two_numbers = days % 100
    last_number = days % 10

    if 11 <= last_two_numbers <= 14:
        return "днів"
    elif last_number == 1:
        return "день"
    elif last_number in [2, 3, 4]:
        return "дні"
    else:
        return "днів"


def seconds_to_time(total_seconds: int) -> str:
    days = total_seconds // (24 * 3600)
    remainder = total_seconds % (24 * 3600)
    hours = remainder // 3600
    remainder = remainder % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{days} {get_day_word(days)}, {hours:02d}:{minutes:02d}:{seconds:02d}"


if __name__ == "__main__":
    s = int(input("Введіть кількість секунд:"))
    print(seconds_to_time(s))
