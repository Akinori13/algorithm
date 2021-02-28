# AtCoder Beginner Contest 185
# A-ABC Preparation
# A = list(map(int, input().split()))

# ans = min(A)

# print(ans)




# B-Smartphone Addiction
n, m, t = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]
AB.append([t,t])

max_n = n
time_now = 0
ans = "Yes"

for ab in AB:
    if n - (ab[0] - time_now) <= 0:
        ans = "No"
    else:
        n -= (ab[0] - time_now)
        n = min(max_n, n + (ab[1] - ab[0]))
        time_now = ab[1]

print(ans)
       
