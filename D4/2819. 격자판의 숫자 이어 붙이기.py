T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, num):
    if len(num) == 7:
        if num not in arr:
            arr.append(num)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                num += str(board[nx][ny])
                dfs(nx, ny, num)
                num = num[:len(num) - 1]


for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]
    # print(board)
    arr = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(board[i][j]))
            visited[i][j] = 1
            visited = [[0] * 4 for _ in range(4)]
    # print(arr)
    print(f'#{test_case} {len(arr)}')