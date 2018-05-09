from time import time
a=[]
def linear_search(num):
    flag=0
    for i in range(0,len(a)):
        if(a[i]==num):
            print("Num found In Linear search")
            flag=1
            return 1
    if(flag==0):
        print("num not found in linear search")
        return 0
def binary_search(num,low,mid,high):
    if(a[mid]==num):
        print("Num found in Binary Search")
        return 1
    elif(low>=mid or mid>=high):
        print("Num not found in Binary Search")
        return 0
    elif(num<a[mid]):
        return binary_search(num,low,int((mid-low)/2),mid)
    elif(num>a[mid]):
        return binary_search(num,mid,mid+int((high-mid)/2),high)


def bubble_sort():
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
def main():
    while(1):
        print("Enter the num to insert. Enter ENTER to discontinue \n")
        val=input()
        if(val==""):
            break
        else:
            a.append(int(val))
    bubble_sort()
    for i in a:
        print(i)
    while(1):
        val=(input("Enter the  Number to be searched\n"))

        if(val ==""):
            break
        else:
            time1 = time()
            binary_search(int(val),0,int(len(a)/2),len(a))
            time2=time()
            print("Time Taken to search in Binary Search + sorting  is ",time2-time1)
            time1=time()
            linear_search(int(val))
            time2=time()
            print("Time taken in linear search", time2-time1)
if __name__=='__main__':
    main()
