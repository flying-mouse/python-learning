tmp = raw_input()  
tmp = tmp.lower()
num = 0
for c in tmp:  
    i = ord(c) - 96  
    if i < 1 or i > 26:  
        i = 0  
    num = i+ num 
print num  
