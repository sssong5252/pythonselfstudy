from collections import defaultdict
class Car:
    #인잇 = 생성자 - 클래스를 바탕으로 객체를 만든다. 밑작업.
    def __init__(self):
        # 처음에는 북쪽을 보고 있다고 가정하자
        self.now_see = 0
        
        # 동서남북 방향으로 움직일수 있는 방향 설정
        #         북 동 남 서 방향 이동 키
        self.dx = [0,1,0,-1]
        self.dy = [1,0,-1,0]
        
        # 현재 위치는 0,0을 기준으로 한다.
        self.now_stand =[0,0]
        
        print("현재 위치: (0,0)")
        print("현자 바라보고 있는 방향(북:0 동:1 남:2 서:3 에 해당!): ", self.now_see)
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
    elif num == 2:
        selected.change_see()
    else:
        return 1
    return 0

def create_car(num):
    for i in range(1, num+1):  # 1,2,3
        car[f'car{i}'] = Car()
        
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