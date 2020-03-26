import os
import sys

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

outfile = "out_text.txt"
  

f = open(outfile, "w") 
  
filename = "sampleImg.png"
text = str(((pytesseract.image_to_string(Image.open(filename).convert('LA'))))) 
#print(pytesseract.image_to_boxes(Image.open(filename)))
text = text.replace('-\n', '')      
f.write(text) 

f.close() 
