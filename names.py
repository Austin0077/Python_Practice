names=['Austin',2,'80*65','Ao46','Lemma']
university=['mmu','jkuat','uon','mku','ku']
marks=[12,42,16,35,70,2,10,15]
print(names)
print(university)
print(marks)
print(university[2])#Slicing we use squre brackets, syntax [a:b], i want to output from Jkuat to MMu.
# ie a=staritng point and b is end point.
print(university[1:3])
print(university[ :3])
print(university[1: ])
print(university[ :-3])
print(university[1:-2])
#concatation
new_list=names+university
print(new_list)
new_list1=[names+university]
print(new_list1)
print(new_list1[0][3])