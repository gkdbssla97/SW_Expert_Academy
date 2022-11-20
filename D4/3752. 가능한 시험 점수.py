T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    score = list(map(int, input().split()))
    visited = [1] + [0] * sum(score)
    res = [0]

    for point in score:
        for j in range(len(res)):
            if not visited[point + res[j]]:
                visited[point + res[j]] = 1
                res.append(point + res[j])
    # print(res)
    print(f'#{test_case} {len(res)}')