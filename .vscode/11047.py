N, K = map(int, input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

result=0
for i in coins:
    if K==0: 
      break
    result += K//i
    K %= i

print(result)