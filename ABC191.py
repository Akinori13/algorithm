# AtCoder Beginner Contest 192 [A - D]
# A-Vanishing Pitch
v, t, s, d = map(int, input().split())
def is_exist(start, end, value):
    if start <= value <= end:
        return True
    else:
        return False

if is_exist(v * t, v * s, d):
    print("No")
else:
    print("Yes")




# B-Remove It
n, x = map(int, input().split())
a = list(map(int, input().split()))

answers = [i for i in a if not i == x]

for i in answers:
    print(i, end=" ")




# C-Digital Graffiti
h, w = map(int, input().split())
s = []

for i in range(h):
    tied_input = input()
    one_line = []
    for j in range(w):
        if tied_input[j] == ".":
            one_line.append(0)
        else:
            one_line.append(1)
    s.append(one_line)

answer = 0
for i in range(1, h):
    for j in range(1, w):
        flg = s[i-1][j-1] + s[i-1][j] + s[i][j-1] + s[i][j]
        if flg%2 == 1:
            answer += 1 

print(answer)

# D-Circle Lattice Points
import math
x, y, r = map(float, input().split())

count = 0

for i in range(math.floor(y-r), math.ceil(y+r)):
    j = math.sqrt(r**2 + (i-y)**2) + x
    print("j+r:", j+r, "j:", j-r)
    print("j+r:", math.floor(j+r), "j:", math.ceil(j-r))
    count += abs(math.floor(j+r) - math.ceil(j-r))
    
print(count)