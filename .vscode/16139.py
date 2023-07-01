import sys
input = sys.stdin.readline
s = input().strip() # 문자열 끝에 개행 문자를 제거합니다.
n = int(input())
re = [[0]*26 for i in range(len(s))]
for i in range(len(s)):
    for j in range(26):
        if ord(s[i])-ord('a')==j:
            re[i][j] = re[i-1][j]+1 
        else:
            re[i][j] = re[i-1][j]
for _ in range(n):
    t, x, y = input().strip().split() # 입력을 받고 개행 문자를 제거합니다.
    x, y = int(x), int(y)
    if x == 0:
        print(re[y][ord(t)-ord('a')])
    else:
        print(re[y][ord(t)-ord('a')] - re[x-1][ord(t)-ord('a')])
