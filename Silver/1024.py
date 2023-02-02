# 백준 1024번 수열의 합 문제
# https://www.acmicpc.net/problem/1024
# Key--> Lx = N - L * (L + 1) / 2

n, l = map(int, input().split())

for i in range(l, 101):
    res = n - (i * (i + 1) / 2)
    print(res)

    if res % i == 0:
        res = int(res / i)

        if res >= -1:
            for j in range(1, i + 1):
                print(res + j)
            break
else:
    print(-1)