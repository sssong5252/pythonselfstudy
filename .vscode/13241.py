import math

# 최대공약수를 구하는 함수
def gcd(a, b):
    return math.gcd(a, b)

# 최소공배수를 구하는 함수
def lcm(a, b):
    return a * b // gcd(a,b)

# 두 수의 최소공배수 계산하기
a, b = map(int, input().split())
print(lcm(a, b))
