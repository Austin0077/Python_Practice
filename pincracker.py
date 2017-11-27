pin=input("Enter your Secret Password(Numerals)")
while pin<0:
	pin=input("Enter your Secret Password(Numerals)")
#for(i=0;i<10000000;i++)
for x in xrange(0,10000000):
	print(x)
	if pin==x:
		print(("Your cracked pin is: ")+str(x))
		break