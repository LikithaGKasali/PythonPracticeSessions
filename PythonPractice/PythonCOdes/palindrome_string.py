# input_String = input()
# if input_String == input_String[::-1]:
#     print("palindrome")
# else:
#     print("not")

input_String = ['kayak', 'deified','hello','ikhu', 'rotator', 'repaper', 'deed', 'peep', 'wow', 'noon']
pali=[]
non_pali=[]
for i in input_String:
    input_list1 = list(i)
    input_list2 = []
    for j in range(len(input_list1)-1, -1, -1):
        input_list2.append(input_list1[j])

    if input_list2 == input_list1:
        pali.append(i)
    else:
        non_pali.append(i)

print(pali)
print(non_pali)
