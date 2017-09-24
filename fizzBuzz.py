def fizzBuzz():
	checkNum=0

while True:
	print('Input an Interger')
	checkNum=input()
	rem=int(checkNum)%5
	rem1=int(checkNum)%3
	if int(checkNum)%5==0 and int(checkNum)%3==0:
		print('Fizzbuzz')
	elif int(checkNum)%5==0:
		print('Buzz')
	elif int(checkNum)%3==0:
		print('Fizz')
	else:
		print(checkNum)
	if rem==0 or rem1==0:
		#print("The number does not much the criterion")
		break
	print("The number does not much the criterion")
fizzBuzz()