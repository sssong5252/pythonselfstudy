import sys
import math

def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)]: return False
    visited[Y.index(x)] = True
    for y in Y:
        if x + y in primes:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
# X.sort()

# 소수 목록을 미리 준비
primes = []
for i in range(2, 2000):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime: primes.append(i)
    else: continue

answers = []
for i in X:
    matched = {}
    if i == X[0]: continue
    if X[0] + i in primes:
        if N == 2:
            answers.append(i)
            break
        # print(i)
        # 첫번째 숫자와 현재 매치된 숫자를 제외한 새 리스트 생성
        Y = [x for x in X]
        del Y[0]
        del Y[Y.index(i)]
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)
    
    # if matched: print(matched)
    if N != 2 and len(matched) == N - 2: answers.append(i)

if not answers:
    answers.append(-1)

answers.sort()

print(' '.join(list(map(str, answers))))