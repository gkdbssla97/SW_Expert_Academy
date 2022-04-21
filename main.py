for test in range(int(input())):
    str1 = input()
    str2 = input()
    pick = {}

    for i in str1:
        if not i in pick:
            pick[i] = 1
    for i in str2:
        if i in pick:
            pick[i] += 1
    print(f'#{test+1} {max(pick.values()) - 1}')
    #print(pick)
'''
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''