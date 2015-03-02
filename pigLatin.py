s = raw_input()
s.lower()
wordlist=s.split(' ')
def fuyinkaitou(word):
    index=1
    if len(word) == 1:
        return word + 'ay'
    else:
        while (word[index] not in 'aeiouy'):
            index += 1
            if index==(len(word)-1):break
        newword=word[index:]+word[:index]+'ay'
        return newword
wordlist2=[]  
for word in wordlist:
	if word[0] in 'aeiou':
		word = word + 'hay'
		wordlist2.append(word)
	else:
		if word[:2] == 'qu':
			word = word[2:] + 'quay'
			wordlist2.append(word)
		else:
			word = fuyinkaitou(word)
			wordlist2.append(word)
print ' '.join(wordlist2)
		