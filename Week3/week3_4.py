#skip = []
for test in range(int(input())):
    N, M = map(int, (input()).split())
    arr = [0 for _ in range(N)]
    ### 행 검사 ###
    for i in range(N):
        arr[i] = list(input())

    char = []
    for start in range(N):
        for j in range(N - M + 1):
            match_cnt = 0
            #print(len(arr[i]), j)
            if arr[start][j:j + M] == arr[start][j: j + M][::-1]:
                print(f'#{test + 1} {"".join(arr[start][j:j+M])}')


        for j in range(N - M + 1):
            match_cnt = 0
            for k in range(M // 2):
                if arr[j + k][start] == arr[j + M - 1 - k][start]:
                    match_cnt += 1
                    #print(match_cnt)
                if match_cnt == M // 2:
                    ans = []
                    for l in range(M):
                        ans.append(arr[j+l][start])
                    print(f'#{test + 1} {"".join(ans)} ')
                    break








'''XYPV*
V P Y X *
0 1 2 3 4
'''

