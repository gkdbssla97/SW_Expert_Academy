def find_book(r, page):
    cnt = 1
    l = 1
    while 1:
        c = int((l + r) / 2)
        #print(c)
        if page == c:
            break
        if c < page:
            l = c
        elif c > page:
            r = c
        cnt += 1
    return cnt
T = int(input())

for test in range(T):
    P, Pa, Pb = map(int, input().split())
    cnt = 0
    cnt_A = find_book(P, Pa)
    cnt_B = find_book(P, Pb)
    if cnt_A > cnt_B:
        print(f'#{test + 1} B')
    elif find_book(P, Pa) < find_book(P, Pb):
        print(f'#{test + 1} A')
    else:
        print(f'#{test + 1} 0')