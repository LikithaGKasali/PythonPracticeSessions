input_list = [11, 1, 2, 3, 4, 10,0, 5, 6, 7, 8, 9]
# print(max(input_list))
# print(len(input_list))
# print(min(input_list))
Ans = 10000
for i in input_list:
    if i < Ans:
        Ans = i

print(Ans)
