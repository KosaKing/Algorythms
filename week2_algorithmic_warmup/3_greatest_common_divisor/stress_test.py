import random
from gcd import gcd

def gcd_naive_solution(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

if __name__ == "__main__":
    for _ in range(1000):
        a, b = random.sample(range(1, 1000000), 2)
        result1 = gcd_naive_solution(a, b)
        result2 = gcd(a, b)
        if result1 != result2:
            print(f"Wrong answer - data(a={a},b={b}) naive result={result1}, quick result={result2}")
            break
    print('Solution is correct.')
