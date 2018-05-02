import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler=logging.StreamHandler()
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Opening a file for reading")
def main(fileName:str):
    try:
        file=open(fileName,'r+')
        data=(file.read())
        print(data)
        newRecords="I am new New Content"
        file.write(newRecords)
    except FileNotFoundError:
        print("file not found")
    finally:
        file.close()
if __name__=='__main__':
    fName=input("Enter the file want to be opened\n")
    main(fName)