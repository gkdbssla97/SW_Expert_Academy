from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        # if (x, y) == (N - 1, N - 1):
        #     return visited[N - 1][N - 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[x][y] + board[nx][ny]:
                    visited[nx][ny] = visited[x][y] + board[nx][ny]
                    q.append((nx, ny))
                    # for j in range(N):
                    #     print(visited[j])
                    # print('---')
    return visited[N - 1][N - 1]
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    # print(board)
    INF = float('INF')
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = 0
    print(f'#{test_case} {bfs(0, 0)}')
    # for i in range(N):
    #     print(visited[i])
'''
011001
010100
010011
101001
010101
111010
'''