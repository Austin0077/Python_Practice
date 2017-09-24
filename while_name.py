name=''
while not name:
	print("Enter you're Name")
	name=input()
print("How Many guests will you have?")
numb_of_guests=int(input())
if numb_of_guests:
	print("Be sure to have Roms for all youre guests")
print('Done')
for i in range(6):
	print('You are so good '+name)