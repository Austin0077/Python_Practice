#This is a guessing game.
import random
secretnumber=random.randint(1,10)
print("I am thinking of a number between 1 AND 10")
# ask the player to guess 5 time.
for guesstaken in range(1,6):
	print('Take A guess.')
	guess=int(input())

	if guess<secretnumber:
		print("The guess is too low.")
	elif guess>secretnumber:
		print("The Guess is Too High.")
	else:
		break #This condtion is the correct guess
if guess == secretnumber:
	print("Good job! You guessed my number in "+ str(guesstaken) +" guesses")
else:
	print("Nope. The number I was thinking of was "+ str(secretnumber))
	