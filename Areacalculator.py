#! usr/bin/python3.5

#A program to calculate area of shapes
pie=3.142
def Rectangle():
	print("Enter Length")
	Length=int(input())
	print("Enter Width")
	Width=int(input())
	area=Length*Width
	print(area)
def Square():
	print("Enter Side")
	Side=int(input())
	area=Side*Side
	print(area)
def Circle():
	print("Enter Radius")
	Radius=int(input())
	circumference=pie*2(Radius)
	area=pie*Radius*Radius
	print (circumference)
	print(area)
def Sphere():
	print("Enter Radius")
	Radius=int(input())
	area=4/3*pie*Radius*Radius
	print(area)
def Triangle():
	print("Enter Base")
	Base=int(input())
	print("Enter Height")
	Height=int(input())
	area=0.5*Base*Height
	print(area)
print("Chose the shape to get the area\n1.Rectangle\n2.Circle\n3.Square\n4.Sphere\n5.Triangle\n6.EXIT")
shape=int(input())
#while shape < 6:
if shape==1:
	Rectangle
	#break
elif shape==2:
	Circle
	#break
elif shape==3:
	Square
	#break
elif shape==4:
	Sphere
	#break
elif shape==5:
	Triangle
	#break
else:
	print("Sorry, Not in menu")

#print(area)