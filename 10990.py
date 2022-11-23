n = int(input())

print(' ' * (n-1) + '*')

for i in range(n-1):
    #print(' ' * i + '*')
    print(' ' * (n-2-i) + '*' + ' ' * (2*i+1) + '*')