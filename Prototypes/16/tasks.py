import sys
sys.setrecursionlimit(2500)

def f1(n):
    if n <= 2:
        return 1
    if n > 2:
        return f1(n-1) + 2 * f1(n-2)

def f2(n):
    if n <= 3:
        return n
    if n > 3:
        return f2(n-3)*n
    
def f3(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + f3(n-1)

def f4(n):
    if n == 1:
        return 2
    if n == 2:
        return 1
    if n > 2:
        return f4(n-2) + f4(n-1)

def f5(n):
    if n == 1:
        return 1
    if n > 1:
        return f5(n-1) + 2**(n-1)

def f6(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return int((3*n + f6(n-3)) / 3)
    if n > 2 and n % 2 != 0:
        return int((7*n + f6(n-1) - f6(n-2)) / 5)