import sys
word  = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":
        i += 1
        while word[i] != ">":
            i += 1
        i += 1
    elif word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        turn = word[start : i]
        turn.reverse()
        word[start : i] = turn
    else:
        i += 1
        
print("".join(word))
        
        