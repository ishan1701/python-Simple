import logging
logger=logging.getLogger(__name__)
logger.setlevel=(logging.INFO)
handler=logging.StreamHandler()
logger.addHandler(handler)
try:
	data=eval(input("Enter the tree size"))
	for i in range(1,data+1):
		for j in range(1,i+1):
			print(j,end=" ")
		print()
except Exception as e:
	logger.error(e)


