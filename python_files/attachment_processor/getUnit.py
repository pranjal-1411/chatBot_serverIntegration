import re

def getUnit(inFile):

    f = open(inFile,"r")
    #Add more such common occuring value 
    # unit_inr = "₹"
    # x = re.search(unit_inr,,re.IGNORECASE)
    # unit_usd = "travel|ola|uber|ride|driver|car|pickup|flight|train|busy"
    ans = 'inr'
    # for line in f:
    #     x = re.search(category_food_pattern,line,re.IGNORECASE)
    #     if x: return 'Food'
    #     x = re.search(category_travel_pattern,line,re.IGNORECASE)
    #     if x: return 'Travel'
    #     x = re.search(category_acco_pattern,line,re.IGNORECASE)
    #     if x: return 'Accomodation'
    f.close()
    return ans


if __name__ == "__main__":
    print(getUnit("out_text.txt"))
