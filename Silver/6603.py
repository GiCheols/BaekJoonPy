# 백준 6603 로또 문제
# (https://www.acmicpc.net/problem/6603)
from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    k = s[0]
    del s[0]
    res = list(combinations(s, 6))
    for i in range(len(res)):
        print(*res[i], end='\n')
    print()