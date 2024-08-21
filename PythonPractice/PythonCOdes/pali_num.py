num = 12321
n = num
rev = 0
while n != 0:
    n1 = n % 10
    rev = rev * 10 + n1
    n = n // 10

if num == rev:
    print("pali")
else:
    print("not-pali")
