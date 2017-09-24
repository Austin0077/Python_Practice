import random

def getAnswer(answerNumber):
	if answerNumber==1:
		return "It is certain"
	elif answerNumber==2:
		return "It's Decidedly so"
	elif answerNumber==2:
		return "Yes"

	elif answerNumber==4:
		return "reply hazy try again"
	elif answerNumber==5:
		return "Ask again later"
	elif answerNumber==6:
		return "Concentrate and ask again"
	elif answerNumber==7:
		return 'My reply is No'
	elif answerNumber==8:
		return "Outlook not so good"
	elif answerNumber==9:
		return "Very doubtful"

r = random.randint(1,9)
fortunate = getAnswer(r)
print(r)
print(fortunate)
print("Hello",end='')
print('World')