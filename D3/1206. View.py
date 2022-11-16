T = 10
# 0 0 3 5 2 4 9 0 6 4 0 6 0 0
for test_case in range(1, T + 1):
    N = int(input())
    board = list(map(int, input().split()))

    cnt = 0
    for i in range(2, len(board) - 2):
        if board[i - 2] < board[i] and board[i + 2] < board[i] \
                and board[i - 1] < board[i] and board[i + 1] < board[i]:
            max_height = max(board[i - 2], board[i - 1], board[i + 1], board[i + 2])
            # print(board[i])
            cnt += board[i] - max_height
            # print(check_building)
    print(f'#{test_case} {cnt}')
