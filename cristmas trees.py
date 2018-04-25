import logging
logger=logging.getLogger(__name__)
logger.setlevel=(logging.INFO)
handler=logging.StreamHandler()
logger.addHandler(handler)
try:
	height=eval(input(("entthe hiegth of tree\n")))
	height=height+2
	for i in range(height,1,-1):
		for j in range(i,0,-1):
			print(" ",end='')
		for k in range(1,height-i+1):
			print("#",end=' ')
		print("\n")
except Exception as e:
	logger.error(e)
		