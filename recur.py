def recur(n):
    if n == 1: return 1
    return n ** 2 + recur(n - 1)
x = 6
print(x * (x + 1) * (2 * x + 1) // 6)
print(recur(x))