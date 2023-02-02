n = int(input())
m = int(input())

list = []

for i in range(1, 101):
    if((i*i >= n) and (i*i <= m)):
        list.append(i*i)

sum = 0
if(len(list) != 0):     # Happy Case: 올바른 경우이므로 예외처리를 else문에 써주는 것이 좋음
    for i in range(0, len(list)):
        sum += list[i]
        min = list[0]
else:                   # Unhappy Case: 예외에 해당하는 경우이므로 얘를 if문에 써주는 것이 좋음
    print(-1)
    exit(0)

print(sum, min, sep='\n')

"""
그리고 if 문에 () 쓰지마세요
"""