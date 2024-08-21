import infinity as infinity

input_list = [11, 3, 4, 10, 5, 6, 7, 8, 9]
# print(max(input_list))
# print(len(input_list))
# print(min(input_list))
Ans = float('inf')
for i in input_list:
    if i < Ans:
        Ans = i

print(Ans)
