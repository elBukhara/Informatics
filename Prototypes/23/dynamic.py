def f1():
    a = [0]*33
    a[2] = 1
    for i in range(3, 33):
        if i % 3 == 0:
            a[i] = a[i//3] + a[i-1]
        else:
            a[i] = a[i-1]
    print(a)   
    print(a[32])