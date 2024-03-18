from turtle import *

def other():
    tracer(0)
    k = 100
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
    