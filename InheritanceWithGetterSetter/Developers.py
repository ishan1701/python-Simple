from InheritanceWithGetterSetter.Employees import Employee

import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler=logging.StreamHandler()
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Developer(Employee):
    def __init__(self,name,ssn,salary,language:[]):
        super().__init__(name,ssn,salary)
        self._skills=language
        logger.info("Developer Initiated")
    @property
    def skills(self):
        print(self._skills)
    @skills.setter
    def skills(self,newLanguage):
        self._skills.append(newLanguage)

def main():
    d1=Developer("Jana Carla",123,39990.90,['Scala'])
    logger.info("Calling getter for fName")
    print(d1.fName)
    logger.info("calling Setter for fName to set new first_name")
    d1.fName="Charles"
    print(d1.fName)
    print(d1.skills)
    logger.info("calling Setter for skills to set new language")
    d1.skills=['Python']
    print(d1.skills)

if __name__=='__main__':
    main()
