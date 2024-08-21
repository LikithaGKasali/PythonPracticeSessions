input_list1 = list(input())
input_list2 = list(input())

# for i in input_list1:
#    if i in input_list2:
#        print(i)

A1= set(input_list1)
A2=set(input_list2)

Ans=A1.intersection(A2)
print(Ans)
