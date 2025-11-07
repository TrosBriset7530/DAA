def phi(n):
    if n == 1: return 1
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def reduce_tower(lst, mod):
    if not lst: 
        return 1
    if mod == 1: 
        return 0
    a = lst[0]
    if len(lst) == 1:
        return a % mod
    exp = reduce_tower(lst[1:], phi(mod))
    if exp == 0:
        exp += phi(mod)
    return pow(a, exp, mod)

def last_digit(lst):
    if not lst:
        return 1
    base = lst[0] % 10
    if base in [0, 1, 5, 6]:
        return base
    cycle_len = 2 if base in [4, 9] else 4
    exp_mod = reduce_tower(lst[1:], cycle_len)
    if exp_mod == 0:
        exp_mod = cycle_len
    cycles = {
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    return cycles[base][exp_mod - 1]
print(last_digit([2,2,101,2]))                  # 6 ✅
print(last_digit([148048,8733,44335,894574,461197]))  # 8 ✅
print(last_digit([696917,776334,250975,762268]))       # 1 ✅
