'''Object Oriented Programming
* Structured Programming
OOp-Java
Ruby
Python
C++
We use object and attributes ie an object is a blueprint
in objects we have behaviours/Methods
Object-Class
Attributes-Class variables
Behaviours /Methods-class functions
Object Instanses-car()giving it memory address.
1.Inheritace in Humanbeing
2.Encapsulation-Hiding
3.Polymorphism-Many forms of somme thing ie Bank account with withdrwa and deposit.
3.'''
#modeling a tiple human being
#Google Io meetup event bright.
class HumanBeing():#Class constructor. Human being has;
	def __init__(self,name="Person",gender="Human",age=20,colour="black",height="5.6",mpesapin=1234,mpesabal=20000):
		#class attributes
		self.name=name
		self.gender=gender
		self.age=age
		self.colour=colour
		self.height=height
		self.__pin=mpesapin
		self.__bal=mpesabal

	#Class Methods
	def speak(self):
		return "I'm {}. Aged{}. Skin colour {}. {}".format(self.name,self.age,self.colour,self.gender)
	def grow(self):
	   self.age+=1

	  # Getters and Setters
	def getBalance(self):
		enterpin=int(input('Enter Pin: '))
		if enterpin== self.__pin:
			print("Mpesa Balances is: ",self.__bal)
		else:
			print("Geta outof here")
		
class Man(HumanBeing):
	def __init__(self,name="Person",gender="Human",age=20,colour="black",height="5.6",mpesapin=1234,mpesabal=20000,beard=True):
		super().__init__(name=name,gender="Male",age=age,colour=colour,height=height,mpesapin=mpesapin,mpesabal=mpesabal)
		self.beard=beard

	def maturity(self):
		if beard:
			print("Mature Male")
		else:
			print("Normal Male")

Janet=HumanBeing()
Janet.name="Janet W"
Janet.gender="female"
Janet.colour="Light skin"
print(Janet.name)
Janet.getBalance()
Janet.grow()
print(Janet.speak())
Nderitu=Man("Nderitu",20,"black",5.2,1234.20000)
print(Nderitu.speak())
Nderitu.grow()
Nderitu.grow()
print(Nderitu.speak())
'''
Nderitu=HumanBeing()
Nderitu.height=5.2
Nderitu.colour="black"
Austin=HumanBeing()
Austin.height=5.2
Austin.colour="Black"
print(Nderitu.height)
print(Nderitu.colour)
print(Nderitu)
print(Austin)'''
