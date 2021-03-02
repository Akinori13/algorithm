# AtCoder Beginner Contest 184
# A-Determinant
A = [list(map(int, input().split())) for _ in range(2)]

def main(array:list) -> int:
    ad = array[0][0] * array[1][1]
    bc = array[0][1] * array[1][0]
    return ad - bc

print(main(A))





# B-Quizzes
n, x = map(int, input().split())
s = input()
count = x

for i in range(n):
    if s[i] == "o":
        count += 1
    else:
        if count == 0:
            pass
        else:
            count -= 1

print(count)




# C-Super Ryuma
RC = [list(map(int, input().split())) for _ in range(2)]
ans = 0
if RC[0][0] == RC[1][0] and RC[0][1] == RC[1][1]:
    pass
elif abs(RC[0][0] - RC[1][0]) + abs(RC[0][1] - RC[1][1]) <= 3:
    ans = 1
elif abs(RC[0][0] - RC[1][0]) == abs(RC[0][1] - RC[1][1]):
    ans = 1
else:
    if abs(RC[0][0] - RC[1][0]) + abs(RC[0][1] - RC[1][1]) <= 6:
        ans = 2
    elif -3 <= abs(RC[0][0] - RC[1][0]) - abs(RC[0][1] - RC[1][1]) <= 3:
        ans = 2
    elif (RC[0][0] + RC[0][1]) % 2 == (RC[1][0] + RC[1][1]) % 2:
        ans = 2
    else:
        ans = 3

print(ans)