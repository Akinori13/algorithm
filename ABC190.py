# AtCoder Beginner Contest 190
# A-Very Very Primitive Game
a, b, c = map(int, input().split())

if c == 0:
    if a > b:
        answer = "Takahashi"
    else:
        answer = "Aoki"
else:
    if a >= b:
        answer = "Takahashi"
    else:
        answer = "Aoki"

print(answer)




# B-Magic 3
n, s, d = map(int, input().split())
magic = [list(map(int, input().split())) for i in range(n)]

answer = "No"
for i in range(n):
    if magic[i][0] < s and magic[i][1] > d:
        answer = "Yes"

print(answer)




# C-Bowls and Dishes
n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
CD = [list(map(int, input().split())) for _ in range(k)]

max_n = 0

for i in range(2**k):
    a = set()
    for j in range(k):
        if ((i >> j) & 1) == 1:
            a.add(CD[j][1])
        else:
            a.add(CD[j][0])

    c = 0
    for ab in AB:
        if ab[0] in a and ab[1] in a:
            c += 1
    max_n = max(max_n, c)  

print(max_n)