from sys import stdin

def move_dice(dice, direction):
    if direction == 1:
        dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
    elif direction == 2:
        dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
    elif direction == 3:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]

N, M, x, y, K = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
dice = [0] * 6

for command in commands:
    nx, ny = x + dx[command], y + dy[command]
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    move_dice(dice, command)
    if _map[nx][ny] == 0:
        _map[nx][ny] = dice[5]
    else:
        dice[5], _map[nx][ny] = _map[nx][ny], 0
    x, y = nx, ny
    print(dice[0])
