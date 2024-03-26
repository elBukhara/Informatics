def task1():
    for x in '0123456789ABCDE':
        ans = (int(f"123{x}5", 15) + int(f"1{x}233", 15))
        if ans % 14 == 0:
            print(x, ans // 14)
            break

def task2():
    for x in '0123456789ABCDE':
        ans = (int(f'{x}3483491', 15) + int(f'4893{x}', 15))
        if ans % 14 == 0:
            print(x, ans // 14)

def task3():
    for n in range(3, 16):
        if int('121', n+1) == int('121', n) + int('13', 16):
            print(n)

def task4():
    for x in range(0, 37):
        ans = (6*37**3 + 5*37**2 + 4*37**1 + x*37**0) + (5*37**3 + x*37**2 + 4*37**1 + 7*37**0)
        if ans % 79 == 0:
            print(x, ans // 79)
            break

def task5():
    for p in range(5, 30):
        for x in range(0, p):
            for y in range(0, p):
                if ((1*p**1 + 2*p**0) * (3*p**1 + 4*p**0)) == (x*p**2 + y*p**1 + 2*p**0):
                    print(p, (y*p**1 + x*p**0))
                    break
                
def task6():
    for x in range(8):
        for y in range(8):
            ans = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
            if ans % 117 == 0:
                print(x, y, ans // 117)
                break

def task7():
    ans = 4**2018 + 2**2018 - 32
    ans = bin(ans)
    ans = ans[2:]
    print(ans.count('1'))
