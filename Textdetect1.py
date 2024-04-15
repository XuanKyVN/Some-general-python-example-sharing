import cv2
from PIL import Image
from pytesseract import pytesseract
camera=cv2.VideoCapture(0)
while True:
    _,image=camera.read()
    cv2.imshow('Text detection', image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('pic/image0.jpg',image)
        break
    camera.release()
    cv2.destroyAllWindows()
    def tesseract():
        path_to_tesseract=r"c:/Program Files/Tesseract-OCR/tesseract.exe"
        imagepath='pic/image0.jpg'
        pytesseract.tesseract_cmd =path_to_tesseract
        text=pytesseract.image_to_string(Image.open(imagepath))
        print(text[:-1])
        tesseract()


