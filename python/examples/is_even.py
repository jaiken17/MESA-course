def is_even(n: int) -> bool:
    if n%2 == 0:
        return True
    else:
        return False

def is_odd(n: int) -> bool:
    if n%2 == 1:
        return True
    else:
        return False


x = 12
y = x + 1

print(x,"is even:",is_even(x))
print(x,"is odd:",is_odd(x))
print(y,"is even:",is_even(y))
print(y,"is odd:",is_odd(y))

print(x,"+",y,"=",x+y,"is even:",is_even(x+y))
print(x,"+",y,"=",x+y,"is odd:",is_odd(x+y))