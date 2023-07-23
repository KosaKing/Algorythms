import random
import timeit
from max_pairwise_product import max_pairwise_product

def MaxPairwiseProductNaive(numbers):
    n = len(numbers)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            product = numbers[i] * numbers[j]
            if product > result:
                result = product
    return result

if __name__ == '__main__':
    for _ in range(10000):
        N = random.randint(2, 100)
        A = [random.randint(0, 1000) for _ in range(N)]
        result1 = MaxPairwiseProductNaive(A)
        result2 = max_pairwise_product(A)
        if result1 != result2:
            print(A)
            print(f"Wrong answer - result1={result1}, result2={result2}")
            break
    print('Solution is correct.')

# elapsed_time = timeit.timeit(max_pairwise_product, number=1000)
# print(elapsed_time)