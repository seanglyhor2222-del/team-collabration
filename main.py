import cv2
import easyocr
import matplotlib.pyplot as plt


image_path = 'H:\Beltei\AI\img\images'

img = cv2.imread(image_path)

reader = easyocr.Reader(['en'])
result = reader.readtext('image.png')

#text = reader.readtext(img)

print(result)