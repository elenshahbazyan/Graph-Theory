def factorial_memoization(n, memoization={}):
    if n in memoization:
        return memoization[n]
    if n <= 1:
        return 1
    memoization[n] = n * factorial_memoization(n - 1, memoization)
    return memoization[n]

print(factorial_memoization(5))  
