from sympy import isprime
def is_prime(func):
    def wrapper(*args, **kwargs):
        o_result = func(*args, **kwargs)
        if o_result == 0 or o_result == 1:
            return f'Не является ни простым, ни составным\n{o_result}'
        elif isprime(o_result) == True:
            return f'Простое\n{o_result}'
        else:
            return f'Составное\n{o_result}'

    return wrapper
'''def is_prime(func):
    def wrapper(*args, **kwargs):
        o_result = func(*args, **kwargs)
        if o_result == 0 or o_result == 1:
            return f'Не является ни простым, ни составным\n{o_result}'
        elif o_result > 1:
            for i in range(2, o_result):
                if o_result % i == 0:
                    return f'Составное\n{o_result}'
            else:
                return f'Простое\n{o_result}'

    return wrapper'''


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result1 = sum_three(3, 3, 6)
print(result1)
result2 = sum_three(0, 3, -2)
print(result2)
