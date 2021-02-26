# AtCoder Beginner Contest 188
# A-Large Digits
a, b = map(int, input().split())

ans = 0

def getTotalDigits(num):
    str_num = str(num)
    total = 0
    for i in range(len(str_num)):
        total += int(str_num[i])
    return total

if getTotalDigits(a) >= getTotalDigits(b):
    ans = getTotalDigits(a)
else:
    ans = getTotalDigits(b)

print(ans)




# C-Gentle Pairs
from decimal import Decimal 
n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]

def getInclination(point1, point2):
    change_of_y = Decimal(point1[1] - point2[1]) 
    change_of_x = Decimal(point1[0] - point2[0])
    inclination = change_of_y / change_of_x
    return inclination

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        if -1 <= getInclination(XY[i], XY[j]) <= 1:
            ans += 1

print(ans)



# C-1-SAT
n = int(input())
S = set([input() for i in range(n)])

ans = "satisfiable"

for s in S:
    if "!" + s in S:
        ans = s
        break

print(ans)