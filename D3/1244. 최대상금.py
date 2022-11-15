T = int(input())

def dfs(change_count):
    global ans

    if not change_count:
        tmp = int(''.join(values))
        if ans < tmp:
            ans = tmp
        return
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            values[i], values[j] = values[j], values[i]
            visited_key = ''.join(values)
            # print(visited_key)
            if visited.get((visited_key, change_count - 1), 1):
                visited[(visited_key, change_count - 1)] = 0
                dfs(change_count - 1)
            values[i], values[j] = values[j], values[i]

for test_case in range(1, T + 1):
    val, change_count = input().split()

    ans = -1
    values = list(val)
    change_count = int(change_count)
    visited = {}
    dfs(change_count)
    print(f'#{test_case} {ans}')