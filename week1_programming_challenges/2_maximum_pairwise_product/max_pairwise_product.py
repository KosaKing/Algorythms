def max_pairwise_product(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0] * sorted_numbers[1]


if __name__ == '__main__':
    _ = input()
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
