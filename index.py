import img2pdf
from PIL import Image
import os

#storing image path

img_path = "F:/Python/image.png"

#storing pdf path

pdf_path ="F:/Python/sample.pdf"

#opening image
image = Image.open(img_path)

#converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

#opening or converting pdf file

file = open(pdf_path,"wb")

#writing pdf file with chunks

file.write(pdf_bytes)

#clone image file
image.close()

#closing pdf file
file.close()

#output
print("successfully made pdf file")