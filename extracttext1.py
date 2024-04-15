
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\tesseract-OCR\tesseract.exe"
image = cv2.imread('pic/pdfimg.png')
# image = cv2.imread('pic/handwrite.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# convert background to White
adaptive = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 11)

#text=pytesseract.image_to_string(image)
#text=pytesseract.image_to_string(grayscale)
text=pytesseract.image_to_string(adaptive)

print(text)
#cv2.imshow("image", image)
#cv2.imshow("gray", grayscale)
cv2.imshow("adapt", adaptive)

cv2.waitKey(0)
