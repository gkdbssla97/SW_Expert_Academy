N, M = map(int, input().split())
r, c, d = map(int, input().split())

visited = [[0] * M for _ in range(N)]
# 북 서 남 동 direction = [0, 3, 2, 1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(N):
    graph = list(map(int, input().split()))

visited[r][c] = 1
cnt = 1
while(1):
    if visited[r][c-1] == 0:


print(visited)