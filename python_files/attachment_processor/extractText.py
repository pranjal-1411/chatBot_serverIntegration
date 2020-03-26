from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os

def generateTextFile( fileName , extension ):
    imagePathList = []
    if(extension == "file" ):
    
        pages = convert_from_path("./"+fileName) 
        image_counter = 1
        for page in pages: 
            filename = "page_"+str(image_counter)+".jpg"
            imagePathList.append(filename)
            page.save(filename, 'JPEG') 
            image_counter = image_counter + 1

    elif(extension == "image"):
        imagePathList.append(fileName)

    outfile = "out_text.txt"
    f = open(outfile, "w") 
    for path in imagePathList:
        text = str(((pytesseract.image_to_string(Image.open(path).convert("LA"))))) 
        text = text.replace('-\n', '')      
        f.write(text) 
        
    return "out_text.txt"
    

if __name__ == "__main__":
    imagePathList = []    
    pages = convert_from_path("./bills/bill3.pdf") 
    image_counter = 1
    for page in pages: 
        filename = "page_"+str(image_counter)+".jpg"
        imagePathList.append(filename)
        page.save(filename, 'JPEG') 
        image_counter = image_counter + 1   
    generateTextFile(imagePathList)


 
