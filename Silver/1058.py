# 백준 1058 친구 문제
# https://www.acmicpc.net/problem/1058

n = int(input())
matrix = [list(input()) for _ in range(n)]
res = 0

for i in range(n):
    friend = 0
    for j in range(n):
        if i == j: continue # 본인인 경우
        if matrix[i][j] == 'Y':
            friend += 1
        elif matrix[i][j] == 'N':
            for k in range(n):
                if matrix[j][k] == 'Y' and matrix[i][k] == 'Y':
                    friend += 1
                    break
    res = max(res, friend)
print(res)