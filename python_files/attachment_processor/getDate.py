import re
import datetime
from datetime import date
from dateutil.parser import parse


def getDate(inFile):

    extractedDate = extractDate(inFile)
    if extractedDate == None : 
        dateObject = findComplexDate(inFile) #if GetDate does not work then we will check with findDate
        if dateObject == None : return None
        return dateObject.date()
    
    dateObject = None
   
    if re.search(r'\d{2}/\d{2}/\d{4}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%d/%m/%Y')
    elif re.search(r'\d{4}/\d{2}/\d{2}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%Y/%m/%d')
    elif re.search(r'\d{4}-\d{2}-\d{2}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%Y-%m-%d')
    elif re.search(r'\d{2}-\d{2}-\d{4}' , extractedDate ) :
        dateObject =  datetime.datetime.strptime( extractedDate , '%d-%m-%Y') 
    
    if dateObject is None : return None
    return str(dateObject.date())
    

def extractDate( inFile ):

    f = open(inFile,"r")
    DatePattern = "((\d{2}/\d{2}/\d{4})|(\d{4}/\d{2}/\d{2})|(\d{4}-\d{2}-\d{2})|(\d{2}-\d{2}-\d{4}))"
    ans = None
    for line in f:
       # print(line)
        x = re.search(DatePattern, line)
        if x :
            ans = x.group()
            print(ans)
            break 
    f.close()
    return ans

def findComplexDate(inFile):
    f = open(inFile, "r")
    ans = None
    for line in f:
        try :
            ans = parse(line, fuzzy_with_tokens=True)
            break
        except Exception:
            pass        
    f.close()
    if ans == None:
        return ans

    return ans[0]  


if __name__ == "__main__":       
    getDate('out_text.txt')
     
    