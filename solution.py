import sys

input = sys.stdin.readline


def take_integer():
    return (int(input()))


def take_list():
    return (list(map(int, input().split())))


def take_string():
    s = input()
    return (list(s[:len(s) - 1]))


def take_variables():
    return (map(int, input().split()))


def main():
    n, h = take_variables()
    friends = take_list()
    width = 0
    for friend in friends:
        if friend > h:
            width += 2
        else:
            width += 1
    print(width)


if __name__ == '__main__':
    main()
