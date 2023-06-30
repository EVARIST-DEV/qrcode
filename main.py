import cv2
import pyqrcode
from pyzbar.pyzbar import decode
import time
import webbrowser

# create a QR code
link = 'www.instagram.com/evarist_ej/?igshid=MzNlNGNkZWQ4Mg%3D%3D'
url = pyqrcode.create(link)
url.png('instagram.png')


# read the QRCode from the folder(IMAGES)
image = cv2.imread('youtubeqrcode.png')
for code in decode(image):
    print(code.type)
    print(code.data.decode('utf-8'))

#read and scanning tht QR code from the webcam
cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _,img=cam.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('QRCode',img)
    if cv2.waitKey(1)==ord('q'):
        break
b=webbrowser.open(str(a))
cam.release(a)
cv2.destroyAllWindows()

