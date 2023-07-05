c = int(input())
m = []
for i in range(n):
    m.append(int(input()))
    
m.sort(reverse = True)
result = []

for j in range(n):
    result.append(m[j]*(j + 1))
    
print(max(result))