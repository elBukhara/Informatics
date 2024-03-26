# 14 Задание ЕГЭ
Все команды возвращают строки

    bin(n) --> 2 система счисления
    oct(n) --> 8 система счисления
    hex(n) --> 16 система счисления

Перевод строк из N записи в десятичную

    int('1010', 2) // 1010 --> 10
    int('2110', 3) // 2110 --> 3

*Если в ручную посчитать, переводя в любую систему:*

    s = 134
    ans = []
    while s > 0:
        ans.append(s % 3)
        s = s // 3
        
    ans = [''.join(str(i)) for i in ans]
    ans = ''.join(ans)
    ans = ans[::-1]
    print(ans)  # --- 11222

## №1
![Задание 1](src/1.png)

## №2
![Задание 2](src/2.png)

## №3
![Alt text](src/3.png)

## №4
![Alt text](src/4.png)

## №5
![Alt text](src/5.png)

## №6
![Alt text](src/6.png)

## №7
![Alt text](src/7.png)