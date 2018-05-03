import os
from functools import reduce

print("----------------------------------read will retrun the contents a single string-----------------------------------------\n")
with open('yield.py','r+') as fileObj:
	print(fileObj.mode)
	data=fileObj.read()
print(data)

print("------------------------readline() will return an iterator like. Helpfull to do operation on singlr line------------------------------------\n")
words=[]
with open('yield.py','r+') as fileObj2:
	while(1):
		line=fileObj2.readline()
		if not line:
			break
		else:
			splitWords=line.split(" ")
			for itr in splitWords:
				words.append(itr)
print(words)

filtered_words=list(filter(lambda x: len(x)>1,words))
print(filtered_words)

mapped_words_with_length=list(map(lambda x:len(x),words))
print(mapped_words_with_length)

length_all_words=reduce(lambda x,y:x+y,mapped_words_with_length)
print(length_all_words)
			
print("-----------------------readlines() return contents as a list----------------------------------------------------\n")

with open('yield.py','r+') as fileObj3:
	line=fileObj3.readlines()
	print(type(line))
	for i in line:
		print(i)

print("-------------------------------Write in files----------------------------------")

with open('yield1.txt','a') as writeObj:
	with open('yield.py','r+') as readObj:
		while(1):
			line=readObj.readline()
			print(line)
			if not line:
				break
			else:
				writeObj.write(line)
