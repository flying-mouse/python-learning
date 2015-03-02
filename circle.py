import math
count = 0
n = int(raw_input())
number = 0
if n >= 2:
    for number in range(2,n):
        for sign in range(2,int(math.sqrt(number) + 1)):
            if number % sign == 0:
                break
        else:
            sushu = number
            sushu_1 = sushu
            weishu = 0
            while sushu_1 != 0:
                weishu += 1
                sushu_1 /= 10
                
            if weishu == 1:
                count += 1
            elif weishu >= 2:
                i = 1
                while i < weishu:
                    number_zhuan = int(sushu/(10**i)+(sushu %(10**i) )* (10 ** (weishu - i)))
                    i += 1
                    for sign2 in range(2,int(math.sqrt(number_zhuan) + 1)):
                        if number_zhuan % sign2 == 0 :
                            i = weishu + 1
                            break
                if i == weishu:
                    count +=1

    print count