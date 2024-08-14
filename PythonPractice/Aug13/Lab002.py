"""
    f"{}" String format concept
    User input - num int -> 10, 100, -1, 2, 3.14 -> input
    9x1 = 9
    9x2 = 18... till 10
"""

input1 = int(input())
for i in range(0,11):
    print(f"{input1} * {i} = {input1*i}")
