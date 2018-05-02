import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler=logging.StreamHandler()
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Employee:
    def splitName(self,name):
        try:
            fname,lname=(name.split(" ")[0],name.split(" ")[1])
            return (fname,lname)
        except Exception as e:
            print(e)
            logger.error("Employee not initiated")
            exit()
    def __init__(self,name,ssn,salary):
        self._first_name,self._last_name=self.splitName(name)
        self._salary=salary
        self.__ssn=ssn
        logger.info("Employee Initiated")
    def printDetails(self):
        print(self._first_name)
        print(self._last_name)
    @property
    def fName(self):
        print(self._first_name)
    @fName.setter
    def fName(self,newFname):
        self._first_name=newFname
