import re

def getAmount(inFile):

    f = open(inFile,"r")
    Amount = "((([0-9]+)\.([0-9]+))|([0-9]+))"
    ans = None
    for line in f:
        x = re.search(Amount, line)
        if x and findPattern(line)  :
            ans = x.group()
    f.close()
    print(ans)
    return ans 

def findPattern( line ):
    
    if re.search(r'Total',line,re.IGNORECASE) : return True 
    # Add other such statements and don't forget to add ignoreCase 
    return False; 

if __name__ == "__main__":
    getAmount("out_text.txt")