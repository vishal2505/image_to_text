import pytesseract as tess
from PIL import Image

image = Image.open('test.png')
text = tess.image_to_string(image)

print(text)