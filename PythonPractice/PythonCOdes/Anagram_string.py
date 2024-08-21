A = "hello"
B = "lloehk"
A_list = sorted([i for i in A])
B_list = sorted([j for j in B])
print(A_list)
if len(A) == len(B):
    if A_list == B_list:
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")