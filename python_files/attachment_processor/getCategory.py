import re

def getCategory(inFile):

    f = open(inFile,"r")
    #Add more such common occuring value 
    category_food_pattern = "food|swiggy|zomato|delivery|order|restaurant"
    category_travel_pattern = "travel|ola|uber|ride|driver|car|pickup|flight|train|bus"
    category_acco_pattern = "hotel|stay|room|accomodation|oyo" 
    ans = None
    for line in f:
        x = re.search(category_food_pattern,line,re.IGNORECASE)
        if x: return 'Food'
        x = re.search(category_travel_pattern,line,re.IGNORECASE)
        if x: return 'Travel'
        x = re.search(category_acco_pattern,line,re.IGNORECASE)
        if x: return 'Accomodation'
    f.close()
    return ans


if __name__ == "__main__":
    print(getCategory("out_text.txt"))
