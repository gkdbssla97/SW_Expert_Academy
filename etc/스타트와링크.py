N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
Members = [i for i in range(N)]

# 스타트와 링크로 나누는 브루트포스 문제 같군.
def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i + 1:], r - 1):
                yield next + [arr[i]]
possible_team = []
ans = 10000

for team in combination(Members, N//2):
    print(team)
    possible_team.append(team)

for i in range(len(possible_team)//2):
    team = possible_team[i]
    print(f'{team}A')
    stat_A = 0
    for j in range(N // 2):
        member = team[j]
        for k in team:
            #print(member, k)
            if not(k == member):
                stat_A += graph[member][k]
        #print("------")

    team = possible_team[-1-i]
    print(f'{team}')
    stat_B = 0
    for j in range(N // 2):
        member = team[j]
        # print(member, team)
        for k in team :
            #print(graph[member][k])
            if not (k == member):
                stat_B += graph[member][k]

    ans = min(ans, abs(stat_A - stat_B))
print(ans)
