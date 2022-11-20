T = int(input())

def contains(block):
    for i in range(1, 10):
        if i not in block:
            return False
    return True

def check_square():
    block = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block.append(board[i][j])
            block.append(board[i][j + 1])
            block.append(board[i][j + 2])
            block.append(board[i + 1][j])
            block.append(board[i + 1][j + 1])
            block.append(board[i + 1][j + 2])
            block.append(board[i + 2][j])
            block.append(board[i + 2][j + 1])
            block.append(board[i + 2][j + 2])
            if not contains(block):
                return False
            block = []
    return True
def check_line(val):
    arr1 = set()
    arr2 = set()
    for i in range(9):
        arr1.add(board[i][val])
    if len(arr1) != 9:
        return False
    for i in range(9):
        arr2.add(board[val][i])
    if len(arr2) != 9:
        return False
    return True
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    if not check_square():
        print(f'#{test_case} {0}')
        continue
    for i in range(9):
        if not check_line(i):
            print(f'#{test_case} {0}')
            flag = 1
            break
    if flag == 0:
        print(f'#{test_case} {1}')
