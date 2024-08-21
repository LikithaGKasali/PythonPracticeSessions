n1 = 12
n2 = 15
n3 = 30
gcd = 0

min_num = min(n1, n2, n3)
for i in range(2, min_num):
    if n1 % i == 0 and n2 % i == 0 and n3 % i == 0:
        gcd = i
        break

print(gcd)
