# n1 = 18
# n2 = 12
# HCF = 1
# if n1 > n2:
#     highest = n1
# else:
#     highest = n2
# for i in range(1, highest):
#     if n1% i == 0 and n2 % i == 0:
#         HCF = i
#
# lcm = n1*n2//HCF
# print(lcm)

n1 = 12
n2 = 15
Ans = 0
highest = max(n1, n2)
smallest = min(n1, n2)
for i in range(highest, n1 * n2 + 1, highest):
    if i % smallest == 0:
        Ans = i
        break
print(Ans)
