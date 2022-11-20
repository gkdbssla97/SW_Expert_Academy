T = int(input())

def clap(num):
    tmp = num
    cnt = 0
    while num != 0:
        val = num % 10
        # print(val)
        if val != 0:
            if val % 3 == 0:
                cnt += 1
        num = num // 10
        # print(num)
    if cnt == 0:
        return tmp
    res = ""
    for i in range(cnt):
        res += "-"
    # if tmp == 33:
    #     print(cnt)
    #     print(res)
    return res

arr = []
# clap(33)
for i in range(1, T + 1):
    arr.append(clap(i))
print(*arr)