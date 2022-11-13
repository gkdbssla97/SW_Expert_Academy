from collections import deque

N = int(input())

for test in range(1, N + 1):
    K = int(input())
    arr = list(map(int, input().split()))
    tmp = -1
    flag = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            flag = 1
            break
    if flag == 0:
        print(f'#{test} 0')
        continue
    else:
        flag = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                flag = 1
                break
        if flag == 0:
            total = 0
            for i in range(len(arr) - 1):
                total += arr[-1] - arr[i]
            print(f'#{test} {total}')
            continue

        p = deque(arr)
        q = []
        total = 0
        while p:
            if not q:
                q.append(p.popleft())
            else:
                val = p.popleft()
                if not p:
                    while q:
                        total += val - q.pop()
                    break
                if q[-1] >= val:
                    q.append(val)
                else:
                    while q:
                        total += val - q.pop()
        print(f'#{test} {total}')