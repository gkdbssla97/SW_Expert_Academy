# BFS
# M개의 치킨집 갯수 빼고 나머지 치킨 집을 빈 칸으로 냅둔다.
# Combination으로 해야 할 듯 if cnt == M (def: crush chik)
    # 각 집마다 치킨집까지의 최소 거리 구함
        # 최소 거리 합쳐서 min 값 구하는 문제.
import math
from collections import deque
import copy
def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i + 1:], r - 1):
                yield next + [arr[i]]

N, M = map(int, input().split())
home, chi = [], []
answer = float('inf')
for i in range(N):
    s = (list(map(int, input().split())))
    for j in range(N):
        if s[j] == 1:
            home.append((i, j))
        elif s[j] == 2:
            chi.append((i, j))
            # Combination으로 해야 할 듯 if cnt == M (def: crush chik)
for case in combination(chi, M):
    dis = 0
    print(f'{case}!')
    # 각 집마다 치킨 집까지의 최소 거리 구함
    for h in home:
        min = float('inf')
        for c in case:
            print(c)
            if min > abs(h[0] - c[0]) + abs(h[1] - c[1]):
                min = abs(h[0] - c[0]) + abs(h[1] - c[1])
        # 최소 거리 합쳐서 min 값 구하는 문제.
        dis += min
    if answer > dis:
        answer = dis
print(answer)