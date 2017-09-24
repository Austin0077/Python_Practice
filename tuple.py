marks=[40,20,30,40,45,55,60]
for i in marks:
	print(i)
#changing value of a list.
marks[3]=90
print(marks)
#tuple differs from list as its values canot be changed, tuple uses brackets.
marks=(20,30,40,60,70,30)
for i in marks:
	print(i)

print(len(marks))
print(max(marks))
print(min(marks))
#converting a tuple to list
"""Commenting on multiple lines on Python"""
""" use the method list to convert it back to a list"""
New=list(marks)
print(New)
#converting list to tuple by Funtion tuple.