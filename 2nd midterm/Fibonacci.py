def fibonacci_memoization(n, memoization={}):
    if n in memoization:
        return memoization[n]
    if n <= 1:
        return n
    memoization[n] = fibonacci_memoization(n - 1, memoization) + fibonacci_memoization(n - 2, memoization)
    return memoization[n]

print(fibonacci_memoization(10))
