def recursive(l, r, P, player, cnt):
    c = int((l + r)/2)
    if c == player:
        return cnt
    if l < player < c:
        cnt += 1
        return recursive(l, c, P, player, cnt)
    elif c < player < r:
        cnt += 1
        return recursive(c, r, P, player, cnt)

T = int(input())

for test in range(T):
    P, A, B = list(map(int, input().split()))
    l, r, cnt = 1, P, 0
    #cnt_A = recursive(l, r, P, A, cnt)
    #cnt_B = recursive(l, r, P, B, cnt)
    #print(cnt_A, cnt_B)
    if recursive(l, r, P, B, cnt) < recursive(l, r, P, A, cnt):
        print(f'#{test + 1} B')
    elif recursive(l, r, P, B, cnt) > recursive(l, r, P, A, cnt):
        print(f'#{test + 1} A')
    else:
        print(f'#{test + 1} 0')