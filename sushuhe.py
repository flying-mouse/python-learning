#the sum of prime number
import math
n = int(raw_input())
sum = 0

for m in xrange(2, n):
    for i in xrange(2, int(math.sqrt(m)+ 1) ):
        if m % i == 0 :
            break
    else:
        sum = m + sum
print sum