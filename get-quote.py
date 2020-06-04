import random


def main_function():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    rnd = random.randint(0, len(quotes) - 1)
    print(quotes[-1])


if __name__ == "__main__":
    main_function()
