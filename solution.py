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


def solution():
    limak, bob = take_variables()
    count = 0
    while limak <= bob:
        limak *= 3
        bob *= 2
        count += 1
    return count


def main():
    print(solution())


if __name__ == '__main__':
    main()
