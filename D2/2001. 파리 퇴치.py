T = int(input())

def kill(x, y):
    total = 0
    for i in range(N):
        for j in range(N):
            total += board[x + i][y + j]
    return total

for test_case in range(1, T + 1):
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(M)]
    max_val = 0
    for i in range(M - (N - 1)):
        for j in range(M - (N - 1)):
            max_val = max(max_val, kill(i, j))
    print(f'#{test_case} {max_val}')