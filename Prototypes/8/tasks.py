from itertools import permutations, product

def task1():
    cnt = 0
    for i in product('123456', repeat=5):
        if i.count('1') == 1:
            cnt += 1
    print(cnt) # ANS = 3125

def task2():
    cnt = 0
    for i in product('ABCD', repeat=6):
        if i.count('A') == 2:
            cnt += 1
    print(cnt) # ANS = 1215
    

def task3():
    cnt = 0
    for i in product('AB123', repeat=4):
        # if ( i.count('A') == 1 and i.count('B') == 0 ) or ( i.count('A') == 0 and i.count('B') == 1 ):
        #     cnt += 1
        if (i.count('A') + i.count('B') == 1):
            cnt += 1
    print(cnt) # ANS = 216

def task4():
    """ Сколько существует трехзначных чисел, записанных в пятиричной системе счисления, в записи которых
        цифры следуют слева направо в невозрастающем порядке?
    """
    cnt = 0
    for i in product('01234', repeat=3):
        if i[0] >= i[1] and i[1] >= i[2]:
            print(i)
            cnt += 1
    print(cnt) # ANS = 35

def task5():
    """ Сколько существует трехзначных чисел, записанных в четверичной системе счисления, в записи которых
        цифры следуют слева направо в строго убывающем порядке?
    """
    cnt = 0
    for i in product('0123', repeat=3):
        if i[0] > i[1] > i[2]:
            print(i)
            cnt += 1
    print(cnt) # ANS = 4

def task6():
    """ Есть трехсимвольный пароль который содержит цифры от 1-9. Сколько различных вариантов шифра можно задать, что
    все цифры в пароле различны?
    """
    # ans = list(permutations('123456789', r=3))
    # print(len(ans))
    cnt = 0
    for i in permutations('123456789', r=3):
        cnt += 1 
    print(cnt) # ANS = 504

def task7():
    """ Шифр кодового знака представляет собой последовательность из четырех букв
    из набора "ТАРАНТУЛ". Сколько различных вариантов шифра можно задать, что все буквы
    в шифре различны?
    """
    cnt = 0
    for i in permutations('ТАРНУЛ', r=4):
        cnt += 1
    print(cnt) # ANS = 360