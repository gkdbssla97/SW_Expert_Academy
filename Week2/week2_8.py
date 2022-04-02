def bubble_sort(pick):
    for i in range(len(pick)):
        for j in range(len(pick) - 1):
            if pick[j] > pick[j+1]:
                pick[j], pick[j + 1] = pick[j + 1], pick[j]
    #print(pick)
    return pick

T = int(input())

for test in range(T):
    N = int(input())
    pick = list(map(int, input().split()))
    bubble_sort(pick)
    result = []
    for i in range(5):
        result.append(pick[len(pick) - i - 1])
        result.append(pick[i])
    print(f'#{test + 1} {" ".join(map(str, result))}')

'''3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''