# a = ['A', "B", "C", "D", "E"]
# m = 5
#
#
# def left(m):
#     b = ''
#     for i in a[:m]:
#         b += i
#     return b
#
#
# def right(m):
#     c = ""
#     for j in a[:m - 1]:
#         c += j
#     return c[::-1]
#
#
# for i in range(m):
#     print(left(i) + right(i))
# a = int(input("enter the number"))
# for i in range(2,a):
#     if a % i == 0:
#         prime = True
#         for j in range(2,i):
#             if i % j == 0:
#                 prime = False
#         if prime == True:
#             print(i)
# import random
#
# rnum = random.randint(1, 100)
# user = 1
# attemtps = 0
# print(rnum)
# while user != rnum:
#     user = int(input("enter the number"))
#     attemtps += 1
# print(attemtps)
# s = input("enter the string")
# characters = ['A', 'C', 'G', 'T']
# tot = []
# for j in s:
#     b = ''
#     for i in range(len(s)):
#         k = s[i]
#         if k in characters[:i]:
#             b += k
#     tot.append(b)
#
# print(tot)