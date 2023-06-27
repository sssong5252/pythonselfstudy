#사칙연산 계산기
# while True:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     sym = str(input("sym = "))
    
#     print("=" * 100)
#     quit = str(input("ys = "))
#     print("=" * 100)
    
#     if(sym == '+'):
#         print("a + b = ", a + b)
#     elif(sym == '-'):
#         print("a - b = ", a - b)
#     elif(sym == 'x'):
#         print("a * b = ", a * b)
#     elif (sym == '/'):
#         print("a / b = ", a / b)
        
#     if (quit == 'y'):
#         break

# 차를 움직이는 클래스 만들어 보기
# 보고있는 방향(동서남북), 움직이는 행동을 고려해서 만들어 보자
from collections import defaultdict
class Car:
    #인잇 = 생성자 - 클래스를 바탕으로 객체를 만든다. 밑작업.
    def __init__(self):
        # 처음에는 북쪽을 보고 있다고 가정하자
        self.now_see = 0
        self.active = False
        # 동서남북 방향으로 움직일수 있는 방향 설정
        #         북 동 남 서 방향 이동 키
        self.dx = [0,1,0,-1]
        self.dy = [1,0,-1,0]
        
        # 현재 위치는 0,0을 기준으로 한다.
        self.now_stand =[0,0]
        
        print("현재 위치: (0,0)")
        print("현재 바라보고 있는 방향(북:0 동:1 남:2 서:3 에 해당!): ", self.now_see)
        print("*********************************************************")
    # 움직이고 현재위치좌표를 변경하는 메서드
    def move(self):
        self.now_stand =[self.now_stand[0]+self.dx[self.now_see], self.now_stand[1]+self.dy[self.now_see]]
        print("이동후 현재 위치 입니다.: ", self.now_stand)
        print("*********************************************************")
    
    def change_see(self):
        self.now_see = (self.now_see+1)%4
        print("우회전 완료, 현재 보고있는 방향 (북:0 동:1 남:2 서:3 에 해당!): ", self.now_see)
        print("*********************************************************")
        
# 객체 선언

car = defaultdict(int)

def action(selected, num):
    if num ==1:
        selected.move()
        selected.active = True
    elif num == 2:
        selected.change_see()
    else:
        return 1
    return 0

def create_car(num):
    for i in range(1, num+1):  # 1,2,3
        car[f'car{i}'] = Car()
    
        #문자열 안에 변수를 넣고 싶으면 에프스프링을 해야 한다.문자열에 변수를 포함하겠다
def crushed(num):
    crush=[]    
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if car[f'car{i+1}'].now_stand == car[f'car{j+1}'].now_stand:
                if car[f'car{i+1}'].active or car[f'car{j+1}'].active:
                    print("!!!!****충돌상태입니다****!!!!")
                    return 0
             
            
car_num = int(input('원하는 차량수를 입력하세요: '))
create_car(car_num)

while(True):
    for i in range(car_num):
        print(f'car{i+1}: ', end='')
        print(car[f'car{i+1}'].now_stand)
    
    K = int(input(f"차량을 선택하세요(1부터 {car_num}중에 하나): "))
    selected_car = car[f'car{K}']
    
    order = int(input("차량 이동 좌표 시뮬레이터 입니다. (1번: 악셀, 2번: 핸들돌리기 3번: 종료하기)"))
    if action(selected_car, order):
        break
    
    crushed(car_num)