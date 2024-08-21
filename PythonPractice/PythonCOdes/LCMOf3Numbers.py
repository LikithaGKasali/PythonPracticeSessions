n1 = 12
n2 = 15
n3 = 30
lcm = 0

max_num = max(n1, n2, n3)
while True:
    if max_num % n1 == 0 and max_num % n2 == 0 and max_num % n3 == 0:
        lcm = max_num
        break
    max_num += 1

print(lcm)
