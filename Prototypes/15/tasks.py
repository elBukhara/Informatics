def task1():
    cnt = 0

    for a in range(100):
        if all(((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6)) for x in range(100) for y in range(100)):
            cnt += 1
            
    print(cnt)
    

def task2():
    def tr(n, m, k):
        return max(n,m,k) < n + m + k - max(n,m,k)
            
    for a in range(100):
        if all((not(tr(x, 11, 16) == (not((max(x, 5)) > 10)) and tr(4, a, x))) for x in range(100)):
            print(a)


def task3():
    for a in range(1000, 0, -1):
        if all((y + 3*x) > a or (x < 20) or (y < 50) for x in range(100) for y in range(100)):
            print(a)
            break
            
# task3()