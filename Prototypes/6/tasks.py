from turtle import *

def task1_self():
    tracer(0)
    k = 30
    
    pendown()
    for i in range(24):
        forward(3*k)
        left(60)
    penup()

    for x in range(-10, 10):
        for y in range(-10, 10):
            setpos(x*k, y*k)
            dot(2)
    done()
    
def task1_auto():
    tracer(0)
    k = 30
    
    pendown()
    begin_fill()
    for i in range(6):
        forward(3*k)
        left(60)
    end_fill()
    penup()

    cnt = 0
    canvas = getcanvas()
    for x in range(-15, 15):
        for y in range(-15, 15):
            if canvas.find_overlapping(x*k, y*k, x*k, y*k,) == (5,):
                cnt += 1
    print(cnt)
    done()
    
def task2():
    tracer(0)
    k = 2
    left(90)
    
    pendown()
    begin_fill()
    for i in range(111):
        forward(123*k)
        right(120)
    end_fill()
    penup()

    canvas = getcanvas()
    cnt = 0
    for x in range(-300, 300):
        for y in range(-300, 300):
            if canvas.find_overlapping(x*k, y*k, x*k, y*k,) == (5, ):
                cnt += 1
    print(cnt)
    done()
     
def task3():
    tracer(0)
    k = 10
    left(90)
    
    pendown()
    right(90)
    begin_fill()
    
    for i in range(3):
        right(45)
        forward(12*k)
        right(45)
    right(315)
    forward(12*k)
    for i in range(2):
        right(90)
        forward(12*k)
    end_fill()
    penup()
    
    canvas = getcanvas()
    cnt = 0
    for x in range(-150, 150):
        for y in range(-150, 150):
            if canvas.find_overlapping(x*k, y*k, x*k, y*k,) == (5, ):
                cnt += 1
    print(cnt)
    done()
    
def task4():
    tracer(0)
    k = 20
    left(90)
    
    pendown()
    begin_fill()
    for i in range(4):
        forward(7*k)
        right(90)
        forward(7*k)
        left(90)
        forward(7*k)
        right(90)
    end_fill()
    penup()
    
    # for x in range(-50, 50):
    #     for y in range(-50, 50):
    #         setpos(x*k, y*k)
    #         dot(2)
    cnt = 0
    canvas = getcanvas()
    for x in range(-15, 15):
        for y in range(-15, 15):
            if canvas.find_overlapping(x*k, y*k, x*k, y*k,) == (5,):
                cnt += 1
    print(cnt)
    done()
    
def task5():
    tracer(0)
    k = 20
    
    left(90)
    
    pendown
    begin_fill()
    for i in range(6):
        right(36)
        forward(10*k)
        right(36)
    end_fill()
    penup
    
    cnt = 0
    canvas = getcanvas()
    for x in range(-40, 40):
        for y in range(-40, 40):
            if canvas.find_overlapping(x*k, y*k, x*k, y*k,) == (5,):
                cnt+=1
    print(cnt)
    done()
    