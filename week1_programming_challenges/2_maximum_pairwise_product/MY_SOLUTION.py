def MPP(first_digit, int_sequence):
    return first_digit * max(int_sequence)


if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().split()))

    print(MPP(a, b))

    