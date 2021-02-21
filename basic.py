# AtCoder Biginners Selection

# PracticeA
# x = int(input())
# y, z = map(int, input().split())
# message = input()

# total = x + y + z

# print(total, message)

# ABC086A
# num1, num2 = map(int, input().split())
# if num1*num2%2 == 0:
#     print("Even")
# else:
#     print("Odd")

# ABC081A
# s1, s2, s3 = input()
# count = 0
# if int(s1) == 1:
#     count += 1
# if int(s2) == 1:
#     count += 1
# if int(s3) == 1:
#     count += 1
# print(count)

# ABC081B
# n = int(input())
# dim = list(map(int, input().split()))

# def getAnswer():
#     flg = True
#     answer = 0
#     while flg:
#         for i in range(len(dim)):
#             if dim[i]%2 == 0 and i == n - 1:
#                 answer += 1
#                 continue
#             elif dim[i]%2 == 1:
#                 flg = False
#                 return answer
#             else:
#                 dim[i] = dim[i]//2
#                 continue

# print(getAnswer())

# ABC087B
# a, b, c, x = [int(input()) for i in range(4)]
# answer = 0

# for num500 in range(0, a + 1):
#     for num100 in range(0, b + 1):
#         for num50 in range(0, c + 1):
#             if num500*500 + num100*100 + num50*50 == x:
#                 answer += 1

# print(answer)

# ABC083B
# n, a, b = map(int, input().split())
# int_x = 1
# total = 0

# while int_x <= n:
#     str_x = str(int_x)
#     if int_x < 10:
#         c = int(str_x[0])
#     elif int_x < 100:
#         c = int(str_x[0]) + int(str_x[1])
#     elif int_x < 1000:
#         c = int(str_x[0]) + int(str_x[1]) + int(str_x[2])
#     else:
#         c = int(str_x[0]) + int(str_x[1]) + int(str_x[2]) + int(str_x[3])

#     if a <= c and c <= b:
#         total += int_x
#         int_x += 1
#     else:
#         int_x += 1

# print(total)


# ABC088B
# n = int(input())
# a = list(map(int, input().split()))
# b = sorted(a)[::-1]
# alice_list = [b[i] for i in range(n) if i%2 == 0]
# bob_list = [b[i] for i in range(n) if i%2 == 1]

# answer = sum(alice_list) - sum(bob_list)
# print(answer)


# ABC085B
# n = int(input())
# d = [int(input()) for i in range(n)]

# e = sorted(d)[::-1]
# f = [e[i] for i in range(n) if i == 0 or e[i] != e[i - 1]]

# print(len(f))


# ABC085C
# n, y = map(int, input().split())
# answers = []

# for a in range(n + 1):
#     for b in range(n + 1 - a):
#         c = n - a - b
#         if 10000*c + 5000*b + 1000*a == y:
#                 answers.append([c, b, a])

# if len(answers) == 0:
#     print(-1, -1, -1)
# else:
#     answer = answers[0]
#     for i in answer:
#         print(i, end=" ")

