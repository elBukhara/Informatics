def f1(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    
    x = f1(start + 1, finish)
    y = f1(start * 3, finish)
    return x+y

# print(f1(2, 32))

def f2(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    x = f2(start + 8, finish)
    y = f2(start * 2, finish)
    z = f2(start + (start-1), finish)
    
    return x + y + z

# print(f2(2, 34))

def f3(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    
    x = f3(start + 2, finish)
    y = f3(start + (start-1), finish)
    z = f3(start + 10, finish)
    
    return x + y + z

# print(f3(8, 45))

def f4(start, finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    
    x = f4(start - 3, finish)
    y = f4(int(start/2), finish)
    
    return x+y

# print(f4(162, 12))

def f5(start, finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    x = f5(start - 1, finish)
    
    s = str(start)
    s = min([int(i) for i in s if i != '0'])
    
    y = f5(start - s, finish)
    
    return x + y
    
# print(f5(33, 12))

def f6(start, finish):
    if start == finish:
        return 1
    if start > finish: 
        return 0
    x = f6(start + 1, finish)
    y = f6(start * 3, finish)
    
    return x + y

def f7(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if start == 6:
        return 0
    if start == 12:
        return 0
    
    return f7(start+1, finish) + f7(start*2, finish) + f7(start+3, finish)

# print(f7(3, 16))

def f8(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if start == 13:
        return 0
    
    x = f8(start + 1, finish)
    y = f8(start + 2, finish)
    z = f8(start * 3, finish)
    
    return x+y+z

# print(f8(1, 9) * f8(9, 15))