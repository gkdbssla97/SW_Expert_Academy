def possible(idx):
    for i in range(idx):
        if row[i] == row[idx] or abs(row[i] - row[idx]) == idx - i:
            return False
    return True

def dfs(idx):
    global result

    if idx == K:
        result += 1
    else:
        for i in range(K):
            row[idx] = i
            if possible(idx):
                dfs(idx + 1)
                
T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    row = [0] * K
    result = 0
    dfs(0)
    print(f'#{test_case} {result}')
