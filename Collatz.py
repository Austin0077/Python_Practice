def collatz():
	global number
	if (number%2)==0:
		print((number//2))
		number=number//2
		return number
	else:
		print(3*number+1)
		number=3*number+1
		return number		

print("Enter a number:")
try: 
	number=int(input())
except ValueError:
	print('Invalid Input\nPlease Enter an Integer')
#collatz(number)
while number!=1:
	collatz()
	