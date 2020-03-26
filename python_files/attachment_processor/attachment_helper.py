import datetime
from datetime import date
import python_files.attachment_processor.extractText as textExtractor
import python_files.attachment_processor.getAmount as amountFinder
import python_files.attachment_processor.getCategory as categoryFinder
import python_files.attachment_processor.getDate as dateFinder
import python_files.attachment_processor.getUnit as unitFinder


# returns data = { 'unit':'inr','amount':'12','date': dateObject , 'category':'Food' }
def processAttachment( fileName , fileType ):
    
    extractTextPath = textExtractor.generateTextFile( fileName , fileType )
    if extractTextPath is None:
        print('Error in Processing')
        return None
    unit = unitFinder.getUnit( extractTextPath ) 
    amount = amountFinder.getAmount( extractTextPath )
    date = dateFinder.getDate( extractTextPath )
    category = categoryFinder.getCategory( extractTextPath )
    
    data = { 'unit':unit,'amount': amount , 'date':date , 'category':category }
    print(data)
    return data

if __name__ == "__main__":
    processAttachment( 'sds','sdf' )   
