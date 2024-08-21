# ----*----
# ---***---
# --*****--
# -*******-
# *********

N=5
for i in range(0,N):
    for space in range(0,N-i-1):
        print("-", end='')
    for star in range(0,(i*2)+1):
        print("*", end='')
    for space in range(0,N-i-1):
        print("-", end='')        
    print()