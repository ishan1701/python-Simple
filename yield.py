def forWithYield(list):
	for i in list:
		yield(i*1,i*2,i*3)
		
##yield will return a generator object
genneratorObject=forWithYield([1,2,3,4])
for i in genneratorObject:
	print(i)