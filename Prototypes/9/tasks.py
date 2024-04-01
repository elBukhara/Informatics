def task1():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/9/txt/1.txt')

    cnt = 0
    for s in f:
        a = list(int(x) for x in s.split())
        
        check1 = len(set(a)) == len(a)
        oddNumbers = [x for x in a if x % 2 != 0]
        evenNumbers = [x for x in a if x % 2 == 0]
        
        if check1 and (len(oddNumbers) > len(evenNumbers)) and (sum(oddNumbers) < sum(evenNumbers)):
            cnt += 1
            
    print(cnt)
    
def task2():
    """В каждой строке электронной таблицы записаны шесть натуральных чисел. Определите, сколько в таблице строк, для которых выполнены следующие условия:
    — в строке встречается ровно четыре различных числа; два из них по два раза, два  — по одному;
    — сумма повторяющихся чисел (без учёта повторений, то есть каждое число входит в сумму один раз) 
      больше суммы неповторяющихся.
    В ответе запишите число  — количество строк, для которых выполнены эти условия.
    """
    
    
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/9/txt/2.txt')
    from collections import Counter
    
    cnt = 0
    for s in f:
        a = list(int(x) for x in s.split())
        repeats = []
        unrepeats = []
        
        dictionary = Counter(a)
        for key, value in dictionary.items():
            if value == 2:
                repeats.append(key)
            else:
                unrepeats.append(key)
        
        if len(set(a)) == 4 and sum(set(repeats)) > sum(unrepeats):
            cnt += 1
            
    print(cnt)            

def task3():
    """Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел. Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
    — в строке есть только два равных числа, остальные 4 различны;
    — среднее арифметическое повторяющихся чисел меньше чем среднее арифметическое остальных чисел строки.
    """
    
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/9/txt/3.txt')
    
    cnt = 0
    for s in f:
        a = list(int(x) for x in s.split())
        
        repeats = [i for i in a if a.count(i) == 2]
        unrepeats = [i for i in a if a.count(i) == 1]
        
        if len(set(repeats)) == 1 and len(unrepeats) == 4:
            if (sum(repeats) / 2) < (sum(unrepeats) / 4):
                cnt += 1
                
    print(cnt)

def task4():
    f = open('C:/Users/Sony/Desktop/Информатика/Prototypes/9/txt/4.txt')
    
    cnt = 0
    for s in f:
        a = list(int(x) for x in s.split())
        
        repeats = [x for x in a if a.count(x) == 4]
        unrepeats = [x for x in a if a.count(x) == 1]
        
        if len(set(repeats)) == 1 and len(unrepeats) == 3:
            if (sum(repeats)/4) > (sum(unrepeats)/3):
                cnt += 1
                print(a)
                
    print(cnt)
    
task4()