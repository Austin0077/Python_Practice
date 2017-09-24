#! /usr/bin/python3.5
# the program will greet you acording to you're age
print('Enter You"re Age:')
d=input()
count=0
if int(d)<10:
	print('Mtoto Enda Ulale')
elif int(d)<20:
	print('Young Adult Enda Ulale')
elif int(d)>30:
	print('Mzee hapa ni mahali pa Vijana')
else:
	print('You are in the write place')
while int(d)<20:
	d=int(d)+1
	print('You need to bemore than '+str(d)+' of age to Access this Site')
	count=count+1
print('You need '+str(count)+' years to achieve adulthood')