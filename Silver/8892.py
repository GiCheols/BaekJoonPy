# 백준 8892 팰린드롬
# https://www.acmicpc.net/problem/8892
from itertools import permutations

for _ in range(int(input())):
    k = int(input())
    words = []
    for _ in range(k):
        words.append(input())
    for i in list(permutations(words, 2)):
        sumWord = i[0] + i[1]
        if(list(sumWord) == list(reversed(sumWord))):
            res = sumWord
            break
    else:   # for-else문: break가 걸리지 않았다면 else문을 실행하쇼
        res = 0
    print(res)