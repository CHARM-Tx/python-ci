"""A simple Python module to ensure the CI is working."""


def add(first: int, second: int):
    return first + second


def main():
    print(add(3, 5))


if __name__ == "__main__":
    main()
