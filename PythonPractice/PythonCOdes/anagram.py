A = 204
B = 2440
A_list = sorted([int(i) for i in str(A)])
B_list = sorted([int(i) for i in str(B)])
if len(str(A)) == len(str(B)):
    if A_list == B_list:
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("not Anagram")
