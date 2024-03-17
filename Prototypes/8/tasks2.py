from itertools import product

def task1():
    """Михаил составляет 6-буквенные коды. В кодах разрешается использовать только буквы А, Б, В, Г, при этом код не может 
    начинаться с гласной и не может содержать двух одинаковых букв подряд. Сколько различных кодов может составить Михаил?
    """
    arr = list(product('АБВГ', repeat = 6))
    cnt = 0
    for i in arr:
        if i[0] != 'А':
            
            check = True
            for letter in range(len(i) - 1):
                if i[letter] == i[letter + 1]:
                    check = False
            if check == True: 
                cnt += 1
    print(cnt) # ANS = 729

task1()

def task2():
    """Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Вот начало списка:
    1.  ААААА
    2.  ААААК
    3.  ААААР
    4.  ААААУ
    5.  АААКА
    ……
    Укажите номер первого слова, которое начинается с буквы К.
    """
    cnt = 0
    for i in product('AКRU', repeat=5):
        cnt += 1
        if i[0] == 'K':
            break
    print(cnt) # ANS = 257

def task3():
    """Алиса составляет 6-буквенные слова из букв МАНГУСТ. Каждая из букв может встречаться сколько угодно раз, 
    причём первой буквой не может быть А, буква У должна встречаться не менее 1 раза. Также в записи должны быть ровно
    две буквы М.Сколько различных слов может составить Алиса?
    """
    arr = list(product('МАНГУСТ', repeat = 6))
    cnt = 0
    for i in arr:
        if (i[0] != 'А') and (i.count('У') >= 1) and (i.count('М') == 2):
            cnt += 1

    print(cnt) # ANS = 9155
  
def task4():
    """Полина составляет коды из букв слова ПОЛИНА. Код должен состоять из 8 букв, любую букву можно использовать 
    произвольное число раз или не использовать вовсе. Полина хочет, чтобы согласных в каждом коде было больше, чем гласных. 
    Сколько кодов, удовлетворяющих этому условию, она сможет составить?
    """
    arr = list(product('ПОЛИНА', repeat = 8))
    cnt = 0
    for i in arr:
        if (i.count('П') + i.count('Л')+ i.count('Н')) > (i.count('О') + i.count('И')+ i.count('А')):
            cnt += 1

    print(cnt) # ANS = 610173
