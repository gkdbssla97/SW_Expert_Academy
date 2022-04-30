# 이건 BFS 맞음
# Combination으로 M개 뽑음 O
# 미로탈출 처럼 +1씩 증가시켜야 함
# 교점일경우 min크기로 라면 풀 수 있을 거 같은데

import copy
from collections import deque

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i + 1:], r - 1):
                yield next + [arr[i]]

def bfs(case):
    global mini
    visited = [[-1] * N for _ in range(N)]
    time = 0
    for i, j in case:
        visited[i][j] = 0
    queue = deque(case)
    cnt = 0

    while queue:
        if cnt == empty:
            break
        (x, y) = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                time = visited[nx][ny]
                queue.append((nx, ny))
                cnt += 1
            elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                time = visited[nx][ny]
                queue.append((nx, ny))
    if cnt == empty:
        mini = min(time, mini)

N, M = map(int, input().split())
#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
virus = []
empty = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            empty += 1

mini = 2500
for case in combination(virus, M):
    bfs(case)

if min == 2500:
    print(-1)
else:
    print(mini)