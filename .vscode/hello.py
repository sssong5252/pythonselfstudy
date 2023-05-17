import turtle as t

t.speed(0)
t.hideturtle()

# x1,y1 - x2,y2 직선 그리기
def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    return

# x,y에 텍스트 쓰기
def write(x,y,text):
    t.up()
    t.goto(x,y)
    t.down()
    t.write(text)
    return

# 좌표평면
line(-500,0,500,0)
line(0,-500,0,500)

# x축 눈금 그리기
i=-500
while i<=500:
    i=i+100
    line(i,-5,i,5)
    if i != 0:
        write(i-10,-20,i)


# y축 눈금 그리기
i = -500
while i <= 500:
    i = i + 100
    line(-5, i, 5, i)
    if i!=0:
        write(7, i-5, i)

t.done()