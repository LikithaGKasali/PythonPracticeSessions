input_string = input()

count = {}
for i in input_string:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count)