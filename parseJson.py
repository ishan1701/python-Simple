import json

class Person:
    def __init__(self,fname,lname,email,genger,ip_address):
        self.name=fname+" "+lname
        self.email=email
        self.gender=genger
        self.ip_address=ip_address
    def getDetails(self):
        print((self.name,self.email,self.gender,self.ip_address))

def main():
    try:
        with open("person.json",'r') as fObj:
            data=json.load(fObj)
        person_List=[]
        for itr in data:
            person_List.append(Person(itr['first_name'],itr['last_name'],itr['email'],itr['gender'],itr['ip_address']))
        for itr in person_List:
            itr.getDetails()
    except Exception as e:
        print(e)
if __name__=='__main__':
    main()



