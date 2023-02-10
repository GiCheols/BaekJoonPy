fibo_one = [0, 1]
fibo_zero = [1, 0]
"""_summary_
fibo_zero.append(1)
fibo_zero.append(0)
fibo_one.append(0)
fibo_one.append(1)
"""

for i in range(2, 41):
    fibo_zero.append(fibo_zero[i-1] + fibo_zero[i-2])
    fibo_one.append(fibo_one[i-1] + fibo_one[i-2])

for _ in range(int(input())):
    n = int(input())
    print(fibo_zero[n], fibo_one[n])