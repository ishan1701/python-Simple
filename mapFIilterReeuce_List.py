import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler=logging.StreamHandler()
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
from functools import reduce

def main():
    myList=[]
    for i in range(1,10):
        myList.append(i)
    logger.info("Implementing Map in List")
    mappedList=(map(lambda x:x+10,myList))
    logger.info(type(mappedList))
    print(list(mappedList))

    logger.info("Implementing Filter in List")
    filteredList=list(filter(lambda x:x%2==0,myList))
    print(filteredList)

    logger.info("Implementing Reduce in List")
    reducedList=reduce(lambda x,y:x+y,myList)
    print(reducedList)
if __name__=='__main__':
    main()