def spam():
	'''This is a multiline comment to help
	explain what the spam() function does.'''
	user=input('What is your name??')
	print('Hello!'+user)
spam()
def austin():
	print('How do You feel?')
	feeling=input()
	n=1
	while n == 1:
		if feeling.lower()== 'great':
			print('I feel Great too.')
		elif feeling.lower()== 'good':
			print('I feel good too')
		else:
			print('Hope the rest of your day is good.')

		print('Do you want to continue?\n1.Yes\n2.EXIT')
		n = input(int())
austin()
'''while net==1:
	austin()'''
