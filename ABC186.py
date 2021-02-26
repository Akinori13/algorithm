# AtCoder Beginner Contest 186
# A-Brick
# n, w = map(int, input().split())

# ans = n//w

# print(ans)




# B-Blocks on Grid
# h, w = map(int, input().split())

# ans = 0
# total = 0
# min_num = 100

# for i in range(h):
#     one_line = list(map(int, input().split()))
#     for j in range(w):
#         min_num = min(min_num, one_line[j])
#         total += one_line[j]

# print(total - min_num*h*w)




# C-Unlucky 7
n = int(input())

count = 0
ans = 0

for i in range(1, n+1):
    str_decimal_i = str(i)
    str_octal_i = format(i, 'o')
    if '7' in str_decimal_i or '7' in str_octal_i:
        count += 1

ans = n - count
print(ans)