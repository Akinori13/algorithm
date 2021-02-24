# AtCoder Beginner Contest 189
# A-Slot
C = input()

answer = "Lost"

if C[0] ==  C[1] == C[2]:
    answer = "Won"

print(answer)




# B-Alcoholic
n, x = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(n)]

total_intake = 0
count = 0
answer = -1
for vp in VP:
    count += 1
    total_intake += vp[0] * vp[1]
    if total_intake > x*100:
        answer = count
        break

print(answer)




# C-Mandarin Orange
n = int(input())
A = list(map(int, input().split()))

ans = 0

for l in range(n):
    min_qty = A[l]
    for r in range(l, n):
        section_length = r - l + 1
        min_qty = min(min_qty, A[r])
        total_qty = section_length * min_qty
        ans = max(ans, total_qty)

print(ans)