T = int(input())

for test_case in range(1, T + 1):
    p = int(input())
    board = [[0] * p for _ in range(p)]

    t = p
    idx = 1
    cur_x, cur_y = 0, 0
    while t > 0:
        # print(f't:{t}')
        a, b, c, d = t, t - 1, t - 1, t - 2
        # print(a, b, c, d)
        if a:
            for cnt in range(a):
                board[cur_x][cur_y] = idx
                cur_y += 1
                idx += 1
            cur_y -= 1
        else: break
        if b:
            cur_x += 1
            for cnt in range(b):
                board[cur_x][cur_y] = idx
                cur_x += 1
                idx += 1
            cur_x -= 1
        else:
            break
        if c:
            cur_y -= 1
            # print(cur_x, cur_y)
            for cnt in range(c):
                board[cur_x][cur_y] = idx
                cur_y -= 1
                idx += 1
            cur_y += 1
        else:
            break
        if d:
            # print(f'final:{cur_x} {cur_y}')
            cur_x -= 1
            for cnt in range(d):
                board[cur_x][cur_y] = idx
                cur_x -= 1
                idx += 1
            cur_x += 1
            cur_y += 1
            # print(f'final:{cur_x} {cur_y}')
        else:
            break
        t -= 2
    print(f'#{test_case}')
    for i in range(p):
        print(*board[i])
    # print()
