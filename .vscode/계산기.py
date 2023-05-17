#사칙연산 계산기
while True:
    a = int(input("a = "))
    b = int(input("b = "))
    sym = str(input("sym = "))
    
    print("=" * 100)
    quit = str(input("ys = "))
    print("=" * 100)
    
    if(sym == '+'):
        print("a + b = ", a + b)
    elif(sym == '-'):
        print("a - b = ", a - b)
    elif(sym == 'x'):
        print("a * b = ", a * b)
    elif (sym == '/'):
        print("a / b = ", a / b)
        
    if (quit == 'y'):
        break
    