import sys

# 입력 단계
input = sys.stdin.readline
n, l = map(int, input().split())

# n만큼 입력을 받으며 시작 지점과 웅덩이 종료 지점을 리스트 형식으로 저장
pools = [list(map(int, input().split())) for _ in range(n)]
pools.sort(key = lambda x: x[0])

cur, res = 0, 0

for start, end in pools:    # start = 1, end = 6
    """ 시간 초과
    if start > end:
        continue
    if cur > start:
        start = cur
    while start < end:
        start += l
        res += 1
    cur = start
    """
    cur = max(start ,cur)
    dist = end - cur
    cnt = (dist + l - 1) // l
    res += cnt
    cur += cnt * l
print(res)