T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = list(map(int, input().split()))

    visited = [0] * 101
    for x in board:
        visited[x] += 1
    max_val = max(visited)
    #print(visited)
    check_max_val = []
    for x in range(len(visited)):
        if visited[x] == max_val:
            check_max_val.append(x)
    #print(check_max_val)
    if len(check_max_val) == 1:
        print(f'#{test_case} {check_max_val[0]}')
    else:
        print(f'#{test_case} {max(check_max_val)}')

# str = "93 29 85 84 5 25 43 70 29 25 61 78 5 80 9 65 7 39 44 91 42 60 38 54 19 31 94 87 68 46 57 52 91 16 95 90 73 32 4 1 92 17 68 67 49 33 3 5 1 80 75 31 40 53 58 2 63 31 87 80 11 50 1 74 31 52 53 70 1 85 6 99 15 35 28 49 75 97 33 25 74 44 18 47 29 47 44 56 69 31 79 7 46 23 95 76 47 38 37 97 79 79 47 60 75 5 23 48 97 70 67 2 83 57 58 90 74 13 77 89 2 77 76 21 100 93 82 64 34 94 31 88 91 77 32 47 38 18 81 70 0 20 41 37 37 17 77 43 99 79 4 34 66 74 4 1 59 38 34 34 0 24 9 76 56 95 51 43 55 51 65 10 73 12 17 66 54 97 52 57 84 65 89 38 55 28 77 98 10 36 93 33 58 99 36 19 77 59 50 35 83 85 87 3 3 63 16 31 17 2 38 27 28 59 29 63 75 52 60 2 3 14 79 28 75 30 39 77 75 65 59 79 2 47 4 29 96 84 37 98 16 56 63 34 75 32 69 80 24 60 3 95 40 57 60 94 22 37 20 79 27 2 59 89 88 37 81 37 11 56 95 33 82 25 76 14 79 81 48 79 53 54 69 95 99 96 98 24 43 81 89 69 71 27 33 61 22 91 55 46 15 83 28 75 34 82 86 61 2 79 3 74 63 56 33 65 87 64 66 22 84 42 100 47 45 23 46 83 68 44 74 77 88 7 47 18 64 87 96 39 74 60 70 57 6 74 65 98 85 89 8 68 87 90 43 41 2 52 75 19 11 35 27 35 65 85 28 41 7 74 39 83 13 61 80 38 74 79 22 39 45 22 81 32 17 95 25 37 99 3 66 42 17 7 56 23 30 7 78 11 74 10 13 72 70 34 95 35 64 42 71 9 95 96 22 81 36 78 19 78 4 33 91 46 3 6 33 5 39 34 54 32 59 24 4 24 80 98 41 32 39 25 63 70 45 98 85 56 24 29 14 75 35 91 93 30 9 81 39 71 47 8 44 100 88 43 49 48 93 6 18 31 74 8 89 95 11 24 1 7 15 61 34 12 34 40 81 72 98 26 41 79 69 51 73 46 31 44 58 90 77 0 6 85 77 59 41 1 8 69 50 50 37 57 63 30 34 24 80 86 81 83 14 76 79 55 51 96 73 64 18 96 100 28 86 82 51 4 73 94 10 18 15 15 55 61 63 27 27 11 7 33 39 66 8 49 7 92 0 6 46 70 38 14 32 77 31 2 23 19 61 29 51 31 69 46 55 37 56 27 31 7 15 13 47 65 35 88 89 0 70 31 6 62 29 36 15 58 61 62 58 24 26 83 77 44 66 47 78 79 88 13 55 74 15 60 13 89 100 94 72 18 62 13 3 14 7 47 93 52 33 69 41 12 9 85 94 19 43 1 12 25 76 82 64 22 53 54 59 90 50 95 6 34 92 31 55 17 9 97 53 77 19 9 10 55 72 48 98 44 37 84 15 6 60 41 39 20 68 1 67 23 74 65 14 76 29 100 70 10 3 12 14 76 12 77 68 36 78 31 53 87 66 49 51 68 97 73 20 29 69 68 32 7 14 60 6 8 87 26 38 33 66 69 82 58 24 42 56 90 42 7 0 84 76 12 34 46 76 13 50 67 65 30 41 91 53 38 66 53 28 10 43 73 46 11 89 73 45 11 8 52 23 89 51 53 9 0 4 78 24 15 27 55 15 82 5 38 16 27 76 11 47 86 80 76 72 11 59 82 21 98 24 60 17 17 61 50 51 0 80 19 85 100 10 62 69 97 85 62 38 11 80 80 61 23 47 35 74 84 42 37 27 34 56 0 23 65 16 86 53 78 72 57 21 90 74 59 24 70 6 77 26 46 20 10 0 41 57 47 32 15 66 64 62 48 21 16 31 27 76 65 80 48 61 40 72 92 92 77 24 16 35 0 52 58 73 91 21 95 69 10 61 18 52 7 37 16 73 0 34 3 0 62 68 48 31 17 95 55 98 23 50 60 16 98 20 17 39 79 95 17 80 27 78 51 59 42 33 35 3 90 6 49 65 16 32 21 79 88 98 13 28 48 51 41 43 36 40 77 98 27 57 47 41 34 92 53 0 77 15 7 40 80 35 45 90 22 91 45 37 50 5 47 33 53 79 69 65 41 67 92 38 85 87 45 24 50 1 54 7 32 1 73 35 73 45 88 68 25 55 21 30 64 4 14 21 48 79 42"
# tmp = []
# # str = str.split(" ")
# for x in str.split(" "):
#     tmp.append(x)
# print(tmp.count("79"))
# print(tmp.count("77"))