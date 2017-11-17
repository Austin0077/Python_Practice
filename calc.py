option=4
while option<6: 
  print "*****MENU********\n1.ADD\n2.Subtract\n3.Divide\n4.Multiplication\n5.Modulus\n6.Exit"
  option=int(input())
  if option==6:
  	break
  x=int(input("Enter 1st Number :"))
  y=int(input("Enter 2nd Number :"))
  if option==1:
  	answer=x+y
  elif option==2:
  	answer=x-y
  elif option==3:
  	answer=x/y
  elif option==4:
  	answer=x*y
  elif option==5:
  	answer=x%y
  else:
  	break

  print "Answer is:%s " %answer #+str(answer)
