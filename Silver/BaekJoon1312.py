a, b, n = input().split()
a = int(a)
b = int(b)
n = int(n)
a %= b
for i in range(n-1):
    a = (a*10)%b
print((a*10)//b)