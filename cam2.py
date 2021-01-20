import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
cap=cv2.VideoCapture(0)
_,image = cap.read()

while True:
    _,image=cap.read(image)
    boxes=pytesseract.image_to_data(image)
    print(boxes)
    for x,boxes in enumerate(boxes.splitlines()):
        if x!=0:
            boxes=boxes.split()
            if len(boxes)==12:
                x,y,w,h=int(boxes[6]),int(boxes[7]),int(boxes[8]),int(boxes[9])
                cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
                cv2.putText(image,boxes[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),3)

                cv2.imshow('image',image)
                k=cv2.waitKey(10) & 0xff
                if k==7:
                    break
cap.release()