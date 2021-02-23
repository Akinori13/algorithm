# AtCoder Beginner Contest 192 [A - D]
# A-Star
# import math

# answer = 0

# x = int(input())
# n = math.ceil(x/100)
# coins = n*100 - x

# if coins > 0:
#     answer = coins
# else:
#     answer = 100

# print(answer)




# B-uNrEaDaBlE sTrInG
# s = input()

# answer = "Yes"

# for i in range(len(s)):
#     if i%2 == 0:
#         if s[i].islower():
#             continue
#         else:
#             answer = "No"
#             break
#     else:
#         if s[i].isupper():
#             continue
#         else:
#             answer = "No"
#             break

# print(answer)




# C-Kaprekar Number
# n, k = map(int, input().split())
# a = [n]

# for i in range(k):
#     el = str(a[i])
#     b = []
#     for j in range(len(el)):
#         b.append(el[j])
#     enLarged_el = sorted(b)[::-1]
#     enSmalled_el = sorted(b)
    
#     str_max_el = ""
#     for j in enLarged_el:
#         str_max_el += j
    
#     str_min_el = ""
#     for j in enSmalled_el:
#         str_min_el += j

#     max_el = int(str_max_el)
#     min_el = int(str_min_el)

#     a.append(max_el - min_el)

# print(a[k])




# D-Base n
# x = input()
# m = int(input())

# d = 0
# for i in range(len(x)):
#     if int(x[i]) > d:
#         d = int(x[i])
#     else:
#         continue

# def binary_search(data, left, right, value):
#     while left <= right:
#         mid = (left + right) // 2
#         el = 0
#         for i in range(len(data)):
#             el += int(data[i])*((mid)**(len(data) - i - 1))
#         if el == value:
#             return mid
#         elif el < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return mid - 1

# # Solve
# if len(x) == 1:
#         if  int(x) <= m:
#             answer = 1
# else:
#     answer = binary_search(x, 0, 10**18, m) - d

# print(answer)