# modify the program and make it count the number of same words in the sentense HINT
from collections import Counter
import re
import pprint

reg=re.compile('\S{3,}')
def words():
	global sentence
	sentence=input("Enter a sentence ")
	new_sentence=sentence.split()
	print(new_sentence)
	#if  name in new_sentence:
	#	count+=1
	#	print(count)
	counted=Counter(ma.group() for ma in reg.finditer(sentence))
	pprint.pprint(counted)


words()

