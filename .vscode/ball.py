from collections import deque

def move_ball(x, y, dx, dy, board):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def find_shortest_path(red_x, red_y, blue_x, blue_y, board):
    queue = deque([(red_x, red_y, blue_x, blue_y, 1)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        curr_red_x, curr_red_y, curr_blue_x, curr_blue_y, d = queue.popleft()
        if d > 10:
            break
        for i in range(4):
            next_red_x, next_red_y, red_cnt = move_ball(curr_red_x, curr_red_y, dx[i], dy[i], board)
            next_blue_x, next_blue_y, blue_cnt = move_ball(curr_blue_x, curr_blue_y, dx[i], dy[i], board)

            if board[next_blue_x][next_blue_y] == 'O':
                continue
            if board[next_red_x][next_red_y] == 'O':
                return d
            if next_red_x == next_blue_x and next_red_y == next_blue_y:
                if red_cnt > blue_cnt:
                    next_red_x -= dx[i]
                    next_red_y -= dy[i]
                else:
                    next_blue_x -= dx[i]
                    next_blue_y -= dy[i]
            queue.append((next_red_x, next_red_y, next_blue_x, next_blue_y, d+1))

    return -1

N, M = map(int, input().split())
board = []
for _ in range(N):
    row = list(input().rstrip())
    board.append(row)

red_x, red_y, blue_x, blue_y = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_x, red_y = i, j
        elif board[i][j] == 'B':
            blue_x, blue_y = i, j

result = find_shortest_path(red_x, red_y, blue_x, blue_y, board)
print(result)
