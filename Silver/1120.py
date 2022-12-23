a, b = map(str, input().split())

if(len(a) != len(b)):
    res = 51
    for i in range(len(b)-len(a) + 1):
        cnt = 0
        for j in range(len(a)):
            if(a[j] != b[i+j]):
                cnt += 1
        res = min(res, cnt)
else:
    res = 0
    for i in range(len(a)):
        if(a[i] != b[i]):
            res += 1
print(res)