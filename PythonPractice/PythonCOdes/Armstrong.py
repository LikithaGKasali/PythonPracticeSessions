num = 1000
Arm_strong = []
for j in range(0, 1000):
    num = str(j)
    count = len(num)
    pow_ans = 0
    num_list = [int(i) for i in num]
    ans_list = sum([pow(i, count) for i in num_list])
    if ans_list == j:
        Arm_strong.append(j)

print(Arm_strong)
