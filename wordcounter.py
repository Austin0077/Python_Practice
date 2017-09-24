def words():
	sentence=input("Enter a sentence").strip()
	sentlist=sentence.split(" ")
	print(sentlist)	
	Dictionery={}
	for eachword in sentlist:
	 	if eachword in Dictionery.keys():
	 		Dictionery[eachword]+=1
	 	else:
	 		Dictionery[eachword]=1
	 	
	print(Dictionery)

words()
