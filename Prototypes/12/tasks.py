def task1():
    s = '1' * 101
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    print(s)
    
def task2():
    word = '4' + 125 * '6' + '4'
    while '63' in word or '644' in word or '6665' in word:
        if '63' in word:
            word = word.replace('63', '4', 1)
        else:
            if '664' in word:
                word = word.replace('664', '5', 1)
            else:
                if '6665' in word:
                    word = word.replace('6665', '3', 1)
    print(word)

def task3():
    ans = set()
    for i in range(2, 1000):
        s = i * '8'
        while '555' in s or '888' in s:
            s = s.replace('555', '8', 1)
            s = s.replace('888', '55', 1)
        ans.add(s)
    print(len(ans))
    
def task5():
    s = 200 * '5'
    while '555' in s or '333' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    # s = '3355' => 3 + 3 + 5 + 5 
    print(sum([int(i) for i in s]))
    
def task6():
    s = '>' + 20*'1' + 15*'2' + 40*'3'
    while '>1' in s or '>2' in s or '>2' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>1', 1)
        if '>3' in s:
            s = s.replace('>3', '1>2', 1)
    s = s.replace('>', '')
    print(sum([int(i) for i in s]))
    # print(sum([int(i) for i in s if i != '>']))
    
def task7():
    for i in range(301, 1000):
        s = i * '5'
        while '555' in s or '888' in s:
            s = s.replace('555', '8', 1)
            s = s.replace('888', '55', 1)
            
        if s.count('5') == s.count('8') == 1:
            print(i)
            break
        
def task8():
    max1 = 0
    min1 = 0
    for i in range(185, 1000):
        s = i * '1'
        while '1111' in s:
            s = s.replace('1111', '2', 1)
            s = s.replace('22', '11', 1)
        
        if s.count('1') > max1:
            max1 = s.count('1')
            min1 = i
            
    print(min1)
    
def task9():
    for a in range(1, 40):
        for b in range(1, 40):
            for c in range(1, 40):
                s = '0' + a*'1' + b*'2' + c*'3' + '0'
                while '00' not in s:
                    s = s.replace('01', '210', 1)
                    s = s.replace('02', '3101', 1)
                    s = s.replace('03', '2012', 1)
                    
                if s.count('1') == 111 and s.count('2') == 101 and s.count('3') == 35:
                    print(a + b + c + 2)
                    break
                
def task10():    
    def check(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(1, 100):
        s = '9' + i*'1' + i*'2'
        while '91' in s or '92' in s:
            if '91' in s:
                s = s.replace('91', '39', 1)
            if '92' in s:
                s = s.replace('92', '59', 1)
                
        ans = sum([int(x) for x in s])
        if len(str(ans)) == 3 and check(ans):
            print(i)
            break
        
def task11():
    from itertools import product
    ans = 100

    for i in product('12', repeat=20):
        s = '0' + ''.join(i) + '0'
        if s.count('1') == 10 and s.count('2') == 10:
            while not '00' in s:
                s = s.replace('012', '30', 1)
                if '011' in s:
                    s = s.replace('011', '20', 1)
                    s = s.replace('022', '40', 1)
                else:
                    s = s.replace('01', '10', 1)
                    s = s.replace('02', '101', 1)
            if s.count('1') == 7 and s.count('2') == 5:
                ans = min(ans, s.count('3'))
    print(ans)
    
def task12():
    from itertools import product

    ans = 0
    for i in product('12', repeat=20):
        i = ''.join(i)
        s = '0' + i + '0'
        if s.count('1') == 10 and s.count('2') == 10:
            while '00' not in s:
                s = s.replace('012', '30', 1)
                if '011' in s:
                    s = s.replace('011', '20', 1)
                    s = s.replace('022', '40', 1)
                else:
                    s = s.replace('01', '10', 1)
                    s = s.replace('02', '101', 1)
            if s.count('1') == 6 and s.count('2') == 5:
                ans = max(ans, s.count('4'))

    print(ans)
    
def task13():
    for i in range(4, 10000):
        s = '5' + i*'2'
        while '52' in s or '1122' in s or '2222' in s:
            if '52' in s:
                s = s.replace('52', '11', 1)
            if '2222' in s:
                s = s.replace('2222', '5', 1)
            if '1122' in s:
                s = s.replace('1122', '25', 1)
        if sum([int(x) for x in s]) == 64:
            print(i)
            break
task13()