#the fifth week 2
import re  
shuru = raw_input()
for word in shuru.split():
    if not re.search(u'^[_a-zA-Z0-9]+$',shuru):  
        print False  
    elif not re.search(u'^[_a-zA-Z]+$',shuru[0]):  
        print False  
    else:  
        print True  
