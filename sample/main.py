"""A simple Python module to ensure the CI is working."""
import requests  # check dependencies are installed


def add(first: int, second: int):
    return first + second


def main():
    requests.Session()  # just exercising the import
    print(add(3, 5))


if __name__ == "__main__":
    main()
