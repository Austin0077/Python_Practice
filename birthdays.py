birthdays={'Alice':'April 1','Bob':'Dec 22','Rozzy':'June 4'}

while True:
	print('Enter a name: (blank to quit)')
	name=input()
	if name=='':
		break

	if name in birthdays:
		print(birthdays[name]+"is the birthday of "+name)
	else:
		print("I do not have birthday information for the "+name)
		print("What is their Birthday?")
		bday=input()
		birthdays[name]=bday
		print[name]=bday
		print("Birthday Database Updated.")
