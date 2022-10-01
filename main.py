import pytesseract as tess
from PIL import Image


tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Location of your tesseract.exe file

img = Image.open('hello.jpg'). # Load the image from explorer

text = tess.image_to_string(img). # Initialize the tesseract

print("Your Text is :\t"+text). # Display the desired output
