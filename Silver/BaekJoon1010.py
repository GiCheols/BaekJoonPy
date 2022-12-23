t = int(input())

def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    return 1

res = []

for i in range(t):
    n, m = map(int, input().split())
    res.append(int(factorial(m)/(factorial(n)*factorial(m-n))))

for i in res:
    print(i)