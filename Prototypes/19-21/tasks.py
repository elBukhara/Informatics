from functools import lru_cache

def task1():
    def moves(s):
        return s+1, s*2

    @lru_cache
    def game(s):
        if any(x >= 129 for x in moves(s)): return "WIN1"
        
        if all(game(x) == 'WIN1' for x in moves(s)): return "LOSS1"
        if any(game(x) == 'LOSS1' for x in moves(s)): return "WIN2"
        if all(game(x) == 'WIN1' or game(x) == 'WIN2' for x in moves(s)): return "LOSS12"
        
    for i in range(1, 129):
        if game(i) == 'LOSS1':
            print(f'19: {i}')
        if game(i) == 'WIN2':
            print(f'20: {i}')
        if game(i) == 'LOSS12':
            print(f'21: {i}')
