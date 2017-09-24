import pprint
birthdays={'Austin':'April 30','Joseph':'August 8','Rozy':'June 04','Hawi':'September 25','Rosa':'October 10'}

while True:
	print("Enter Your name:(Blank to quit)")
	name=input()
	if name=='':
		break
	if name in birthdays:
		print(birthdays[name]+" is the birthday of "+ name)
	else:
		print("I do not have birthday information for "+name)
		print("What is your birthday?")
		bday=input()
		birthdays[name]=bday
		print('Birthday database updated.')

for a in birthdays.values():
	print(a)

for b in birthdays.keys():
	print(b)
for c in birthdays.items():
	print (c)

birthdays.setdefault('color','white')
wewe=input('A sentence you like\n')
wewe=wewe.strip()
count={}

for character in wewe:
	count.setdefault(character,0)
	count[character]=count[character]+1

pprint.pprint(count)