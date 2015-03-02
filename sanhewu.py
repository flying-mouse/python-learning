# the problem about the 3 and 5
n = int(raw_input())
sum = 0
for i in range(0, n):
    if i % 3 == 0 or i % 5 == 0:
        sum = i + sum
else:
    print sum