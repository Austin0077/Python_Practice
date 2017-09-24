def fizzBuzz():
	fizzBuzzNum=False
	while not fizzBuzzNum:
		try:
			checknum=int(input("Input Numbers."))
			divisibleby5=(checknum%5==0)
			divisibleby3=(checknum%3==0)
			if divisibleby5 and divisibleby3:
				print("FizzBuzz")
				fizzBuzzNum=True
			elif divisibleby5:
				print("Buzz")
				fizzBuzzNum=True
			elif divisibleby3:
				print("Fizz")
				fizzBuzzNum=True
			else:
				print("No fizzBuzz Number")
		except ValueError:
			print("Invalid input\n Input a number")

fizzBuzz()
	
