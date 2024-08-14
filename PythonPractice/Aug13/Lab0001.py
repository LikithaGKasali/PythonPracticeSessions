"""
    Create a program , take 2 inputs from the user num1, num2 and give them
    max
    pow num1 to num2
    sub, mul, sum, div.
    Format your out with f{""}
"""

num1 = int(input())
num2 = int(input())
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 // num2
print(add)
print(sub)
print(mul)
print(div)
print(max(num1, num2))
print(pow(num1, num2))

print(f"{add} {sub} {mul} {div}")

