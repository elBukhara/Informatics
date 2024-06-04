from fnmatch import *

def task1():
    
    for i in range(0, 10**8, 317):
        if fnmatch(str(i), "12??1*56"):
            print(i, i // 317)
            
task1()