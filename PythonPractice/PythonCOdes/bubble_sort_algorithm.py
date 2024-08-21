input_num = [1, 4, 5, 2, 6, 7, 4, 3, 2, 2]

for j in range(0, len(input_num) - 1):
    for i in range(0, len(input_num) - 1):
        if input_num[i] > input_num[i + 1]:
            input_num[i + 1], input_num[i] = input_num[i], input_num[i + 1]

print(input_num)
