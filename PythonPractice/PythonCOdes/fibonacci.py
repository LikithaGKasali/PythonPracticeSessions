Range = 10
first = 0
sec = 1
print(first)
print(sec)
for i in range(2, Range):
    Ans = first + sec
    first = sec
    sec = Ans
    print(Ans)
