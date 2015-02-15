n = int(raw_input())
sum = 0
for i in range(0, n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
else:
    print sum