import sys

input = sys.stdin.readline


def take_integer():
    return int(input())


def take_list():
    return list(map(int, input().split()))


def take_string():
    s = input()
    return list(s[: len(s) - 1])


def take_variables():
    return map(int, input().split())


def solution():
    n = take_integer()
    arr = take_list()
    for x in range(n):
        print(arr.index(x+1)+1)


def main():
    solution()


if __name__ == "__main__":
    main()
