# BFS (상하좌우)
# 2차원배열 반시계 이동

R, C, T = map(int, input().split())
graph = []
up = -1
down = -1
for i in range(R):
    graph.append(list(map(int, input().split())))
    if graph[i][0] == -1 and up == -1:
        up = i
        down = i + 1


def spread():
    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    tmp_graph = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        tmp_graph[nx][ny] += graph[i][j] // 5
                        cnt += graph[i][j] // 5
                graph[i][j] -= cnt
    for i in range(R):
        for j in range(C):
            graph[i][j] += tmp_graph[i][j]

def air_up():
    # 동 북 서 남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    d = 0
    before = 0
    x, y = up, 1 # 공기청정기 UP 위치
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

def air_down():
    # 동 남 서 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    before = 0
    x, y = down, 1 # 공기청정기 UP 위치
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny

for _ in range(T):
    spread()
    # for i in range(R):
    #     print(graph[i])
    # print("------------")
    air_up()
    # for i in range(R):
    #     print(graph[i])
    air_down()

sum = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            sum += graph[i][j]
print(sum)


