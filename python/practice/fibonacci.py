from math import sqrt, pow

def next_fibonacci(i1: int, i2: int) -> int:
    return i1 + i2

def print_fibonacci_numbers(n_max: int):

    n0 = 0
    n1 = 1

    print(f"n = {0}, f(n) = {n0}")
    print(f"n = {1}, f(n) = {n1}")

    last = n0
    current = 1
    for n in range(2,n_max):
        temp = current
        current = next_fibonacci(last,current)
        last = temp
        print(f"n = {n}, f(n) = {current}")



def explicit_fibonacci(n: int) -> int:
    sqrt_5 = sqrt(5.0)
    phi = (1 + sqrt_5)/2.0
    phi_conj = (1 - sqrt_5)/2.0
    phi_n = pow(phi,n)
    phi_conj_n = pow(phi_conj,n)
    f_n =  (phi_n - phi_conj_n)/sqrt_5
    return round(f_n)

def print_explicit_fibonacci_numbers(n_max: int):

    for n in range(n_max):
        f_n = explicit_fibonacci(n)
        print(f"n = {n}, f(n) = {f_n}")




print_fibonacci_numbers(20)
print_explicit_fibonacci_numbers(20)