import random


def main_function():
    with open("quotes.txt") as fh:
        quotes = [line.strip() for line in fh]

    rnd = random.randint(0, len(quotes) - 1)
    print(quotes[rnd])


if __name__ == "__main__":
    main_function()
