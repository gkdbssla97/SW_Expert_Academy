N, M = map(int, input().split())
r, c, d = map(int, input().split())

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 0북 1동 2남 3서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

visited_map = [[0] * M for _ in range(N)]
visited_map[r][c] = 1 # 1은 청소
cnt = 1
turn_time = 0
while (True):
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]
    if graph[nx][ny] == 0 and visited_map[nx][ny] == 0:
        r, c = nx, ny
        cnt += 1
        visited_map[r][c] = 1
        # turn_time = 0
    else:
        turn_time += 1
    if turn_time == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if graph[nx][ny] == 1:
            break
        else:
            r, c = nx, ny
        turn_time = 0
print(cnt)


