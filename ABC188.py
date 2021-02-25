# AtCoder Beginner Contest 188
# A-Three-Point Shot
x, y = map(int, input().split())

ans = "No"

if min(x, y) + 3 > max(x, y):
    ans = "Yes"

print(ans)




# B-Orthogonality
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = "No"
total = 0

for i in range(n):
    total += A[i] * B[i]

if total == 0:
    ans = "Yes"

print(ans)




# C-ABC Tournament
n = 2**(int(input()))
A = list(map(int, input().split()))

ans = 0

max_left = 0
left_winner = 0
for i in range(0, len(A)//2):
    if A[i] > max_left:
        max_left = A[i]
        left_winner = i

max_right = 0
right_winner = 0
for i in range(len(A)//2, n):
    if A[i] > max_right:
        max_right = A[i]
        right_winner = i

if max_left > max_right:
    ans = right_winner + 1
else:
    ans = left_winner + 1 

print(ans)