import sys


def take_integer():
    return int(input_func())


def take_list():
    return list(map(int, input_func().split()))


def take_string():
    s = input_func()
    return list(s[: len(s) - 1])


def take_variables():
    return map(int, input_func().split())


def solution():
    n = take_integer()
    cities = take_list()
    for i in range(n):
        if i == 0:
            nearest = abs(cities[i] - cities[i + 1])
        elif i == n - 1:
            nearest = abs(cities[i] - cities[i - 1])
        else:
            nearest = min(
                abs(cities[i] - cities[i - 1]), abs(cities[i] - cities[i + 1])
            )
        farthest = max(abs(cities[i] - cities[-1]), abs(cities[i] - cities[0]))
        print(f"{nearest} {farthest}")


def main():
    while True:
        try:
            solution()
            print()
        except ValueError:
            break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as file:
            input_func = file.readline
            main()
    else:
        input_func = sys.stdin.readline
        main()
