#! usr/bin/python3.5
import random

def inputa():
	print("******WELCOME******")
	print("How many times do you wish to play?")
	num=int(input())
	return num


def process():
	num=inputa()
	sec_no=2
	#sec_no.random()
	total=0
	z=0
	while True:
		if z<=num:
			break
		z=z+1
		print(str(num))
		print("Enter your lucky number "+str(z))
		lucky=int(input())
		x=lucky%sec_no
		if x==0:
			total=total+1
		else:
			y=x%5
			if y==0:
				total=total+3
			else:
				total=total-3
	return total

def output():
	total=process()
	print(total)
	if total>0:
		print("You Win!!")
	else:
		print("You Lose'-'")
output()
