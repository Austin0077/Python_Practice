while True:
	print('Who Are you?')
	name=input()
	if name != 'Joe':
		continue
	print("Hello, Joe. What si the Password? (It is A fish.)")
	password=input()
    if password=='swordfish':
   	break
print('Access Granted.')