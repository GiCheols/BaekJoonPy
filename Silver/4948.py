from math import sqrt

def is_prime():
    prime = [True] * (123456 * 2 + 1)
    m = int(sqrt((123456 * 2 + 1)))
    for i in range(2, m+1):
        if prime[i]:
            for j in range(i+i, (123456 * 2 + 1), i):
                prime[j] = False
    return prime
        
a = is_prime()

while True:
    n = int(input())
    count = 0
    if n == 0:
        exit()
    elif n == 1:
        print("1")
    else:
        for i in range(n + 1, n*2 +1):
            if a[i]:
                count += 1
        print(count)