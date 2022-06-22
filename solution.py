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
    n = take_integer()
    uniforms = []
    count = 0
    for i in range(n):
        x, y = take_variables()
        uniforms.append(x)
        uniforms.append(y)
    for i in range(0, n * 2, 2):
        for j in range(1, n * 2, 2):
            if uniforms[i] == uniforms[j]:
                count += 1
    return count


def main():
    print(solution())


if __name__ == '__main__':
    main()
