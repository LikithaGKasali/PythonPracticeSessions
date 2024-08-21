input_num = [1, 4, 5, 2, 6, 7, 4, 3, 2, 2,7,7]
ans = {}

for i in input_num:
    if i in ans:
        ans[i] = ans[i] + 1
    else:
        ans[i] = 1
print(ans)
for i in ans:
    if ans[i] > 1:
        print(i)
