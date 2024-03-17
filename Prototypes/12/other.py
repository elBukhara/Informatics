def other1():
    s = 68 * '8'
    while '222' in s or '888' in s:
        if '222' in s:
            s = s.replace('222', '8', 1)
        else:
            s = s.replace('888', '2', 1)       
    print(s)
    
def other2():
    min_length = 0
    min_ones = 10000
    for i in range(101, 200):
        s = i * '1'    
        while '101' in s:
            s = s.replace('111', '22', 1)
            s = s.replace('222', '11', 1)
        print(i, s)        
      # if s.count('1') < min_ones:
        #     min_ones = s.count('1')
        #     min_length = i
            
    # print(min_length)
    
def other3():
    s = '1' + 99*'8' + '1'
    while '81' in s or '882' in s or '8883' in s:
        if '81' in s:
            s = s.replace('81', '2', 1)
        else:
            if '882' in s: 
                s = s.replace('882', '3', 1)
            else:
                s = s.replace('8883', '1', 1)
    print(s)