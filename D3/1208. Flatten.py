T = 10

for test_case in range(1, T + 1):
    change_cnt = int(input())
    box = list(map(int, input().split()))

    cnt = 0
    gap = 0
    while cnt <= change_cnt:
        max_val = max(box)
        min_val = min(box)
        gap = box[box.index(max_val)] - box[box.index(min_val)]
        if gap == 1:
            break
        box[box.index(max_val)] -= 1
        box[box.index(min_val)] += 1
        cnt += 1
    # print(box)
    print(f'#{test_case} {gap}')
'''
2
5 8 3 1 5 6 9 9 2 2 4
'''