from collections import deque
import copy

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    cnt = 0
    tmp_graph = copy.deepcopy(graph)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    while queue:
        (x, y) = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if tmp_graph[nx][ny] == 1:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))
    for i in range(N):
        cnt += tmp_graph[i].count(0)

    global answer
    answer = max(answer, cnt)
    return answer

def make_wall(start, cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(start, N*M):
        x = int(i / M)
        y = int(i % M)
        if graph[x][y] == 0:
            graph[x][y] = 1
            make_wall(i + 1, cnt + 1)
            graph[x][y] = 0

answer = 0
make_wall(0, 0)
print(answer)