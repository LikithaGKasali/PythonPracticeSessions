num_input = 100

prime_num = []
for j in range(0, num_input + 1):
    count = 0
    for i in range(1, j + 1):
        if j % i == 0:
            count = count + 1

    if count == 2:
        prime_num.append(j)

print(prime_num)
