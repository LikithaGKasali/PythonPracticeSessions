n1 = 18
n2 = 12
HCF = 1
if n1 < n2:
    smallest = n1
else:
    smallest = n2
for i in range(1, smallest):
    if n1% i == 0 and n2 % i == 0:
        HCF = i

print(HCF)
