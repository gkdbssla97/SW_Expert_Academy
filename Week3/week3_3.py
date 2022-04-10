T = int(input())

#skip = []
for test in range(T):
    result = True
    str1 = input()
    str2 = input()

    skip = list(reversed(str1))
    # print(skip)
    Match_cnt, Now_idx = 0, len(str1) - 1
    while Match_cnt != len(str1) and Now_idx < len(str2):
        if str2[Now_idx] in skip:
            print(str2[Now_idx], skip)
            if str2[Now_idx] == skip[Match_cnt]:
                Match_cnt += 1
                Now_idx -= 1
                continue
            else:
                Match_cnt = 0
                Now_idx += skip.index(str2[Now_idx])
        else:
            Match_cnt = 0
            Now_idx += len(str1)

    if Match_cnt == len(str1):
        print(f'#{test + 1} 1')
    else:
        print(f'#{test + 1} 0')


'''XYPV*
V P Y X *
0 1 2 3 4
'''

