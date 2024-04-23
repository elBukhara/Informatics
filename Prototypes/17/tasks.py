def f1():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.1.txt')
    
    a = [int(x) for x in f]
    pairs = 0
    max_sum = 0
    
    for i in range(len(a) -1):
        if a[i] % 5 == 0 and a[i+1] % 5 == 0:
            pairs += 1
            max_sum = max(max_sum, a[i] + a[i+1])
    
    print(pairs, max_sum)    
    
# f1()

def f2():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.2.txt')
    a = [int(x) for x in f]
    pairs = 0
    max_multiply = 0
    
    for i in range(len(a)-1):
        if (a[i] + a[i+1] > 135) and ((a[i] % 2 != 0) or (a[i+1] % 2 != 0)):
            pairs += 1
            max_multiply = max(max_multiply, (a[i] * a[i+1]))
    
    print(pairs, max_multiply)
    
# f2()

def f3():
    from math import sqrt
    def check(n):
        if n >= 0:
            x = sqrt(n)
            return (x == int(x))
        return False

    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.3.txt')
    a = [int(x) for x in f]
    
    pairs = 0
    min_multiply = 1000
    
    for i in range(len(a)-1):
        if check(a[i]) or check(a[i+1]):
            pairs += 1
            min_multiply = min(min_multiply, (abs(a[i]- a[i+1])))
    
    print(pairs, min_multiply)
    
# f3()

def f4():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.4.txt')
    a = [int(x) for x in f]
    min_item = min(a)
    
    pairs = 0
    max_sum = 0
    
    for i in range(len(a)-1):
        if (a[i] % 123 == min_item) or (a[i+1] % 123 == min_item):
            pairs += 1
            max_sum = max(max_sum, (a[i] + a[i+1]))
    
    print(pairs, max_sum)
    
# f4()

def f5():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.5.txt')
    a = [int(x) for x in f]
    
    # min_int = min([x for x in a if 9 < x < 100])
    min_int = 10
    pairs = 0
    max_sum = 0

    for i in range(len(a)-1):
        if ((len(str(a[i])) == 2 and len(str(a[i+1])) != 2) or (len(str(a[i])) != 2 and len(str(a[i+1])) == 2)) and ((a[i] + a[i+1]) % min_int == 0):
            pairs += 1
            max_sum = max(max_sum, (a[i] + a[i+1]))

    print(pairs, max_sum)
    
# f5()

def f6():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.6.txt')
    
    a = [int(x) for x in f]
    
    min_value = min([x for x in a if x > 0 and str(x)[-2:] == '13']) # 113 
    
    pairs = 0
    max_sum = 0
    
    for i in range(len(a)-1):
        if (a[i] * a[i+1] < 0) and ((a[i] * a[i+1]) % min_value == 0):
            pairs += 1
            max_sum = max(max_sum, (a[i] + a[i+1]))
            
    print(pairs, max_sum)    

# f6()

def f7():
    def check(pair):
        cnt = 0
        for x in pair:
            if len(str(abs(x))) == 5:
                cnt += 1
        if cnt == 2:
            return True
        return False
    
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.7.txt')
    
    a = [int(x) for x in f]
    max_value = max([x for x in a if x > 0 and x % 100 == 29]) # 99429
    
    pairs = 0
    max_sum = 0
    
    for i in range(len(a)-2):
        pair = [a[i], a[i + 1], a[i + 2]]
        if check(pair):
            if sum(pair) <= max_value:
               pairs += 1
               max_sum = max(max_sum, sum(pair))
               
    print(pairs, max_sum)

# f7()

def f8():
    def check(pair):
        cnt = 0
        for x in pair:
            if len(str(abs(x))) == 4:
                cnt += 1
        if cnt == 1:
            return True
        return False

    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/17/files/17.8.txt')
    
    a = [int(x) for x in f]
    max_value = max([x for x in a if len(str(abs(x))) == 4 and str(x)[-2:] == '39']) # 9239
    
    pairs = 0
    max_sum = 0
    
    for i in range(len(a)-1):
        pair = [a[i], a[i+1]]
        if check(pair) and ((sum(pair))**2 <= (max_value**2)):
            pairs += 1
            max_sum = max(max_sum, sum(pair))
            
    print(pairs, max_sum)
    
# f8()