#comprehension in list
from functools import reduce

def list_comprehension(list):
    #map using comprehension
    mapExample=[n*n for n in list]
    print(mapExample)
    #filter using comprehension
    filterExample=[n for n in list if n%2==0]
    print(filterExample)
    #reduce using comprehension
    #redudce in python
    reduceExample=reduce(lambda x,y:x+y,list)
    print(reduceExample)
    
def setComprehension(set):
    mapExample={n*n for n in set}
    print(mapExample)
    filterExample = {i for i in set if i % 2 == 0}
    print(filterExample)
    reduceExample = reduce(lambda x, y: x + y, set)
    print(reduceExample)

def main():
    list=[1,2,3,4,5,6,7,8,9,10]
    #list_comprehension(list)
    mySet=set()
  #  print(type(set))
    for i in range(1,10):
        mySet.add(i)
    setComprehension(mySet)
if __name__=='__main__':
    main()
