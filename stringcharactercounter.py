#write a program that counts the number of characters in a sentense
import pprint
print("Enter a Sentence")
Sentence=input()
count={}
for character in Sentence:
	count.setdefault(character,1)
	count[character]=count[character]
print(len(Sentence))

print(count)
