import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Location of your tesseract.exe file

img = Image.open('hello.jpg')

text = tess.image_to_string(img)

print("Your Text is :\t"+text)
