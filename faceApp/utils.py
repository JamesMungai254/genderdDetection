import cv2 as cv
from models import Image


    



"""
def get_filtered_img(image,action):
    img = cv.cvtColor(image,cv.COLOR_BGR2RGB)
    
    if action== 'NO_FILTER':
        filtered = img
    elif action=='COLORIZED':
        filtered = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    elif action=='GRAYSCALE':
        filtered = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    elif action=='BLURRED':
        width,height = img.shape[:2]
        if width>500:
            k = (50,50)
        elif width>200 and width <=500:
            k=(25,25)
        else:
            k=(10,10)
        blur = cv.blur(img,k)
        filtered = cv.cvtColor(blur,cv.COLOR_BGR2RGB)
    elif action== 'BINARY':
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        _,filtered = cv.threshold(gray,100,255,cv.THRESH_BINARY)
    elif action == 'INVERT':
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        _,img = cv.threshold(gray,100,255,cv.THRESH_BINARY)
        filtered = cv.bitwise_not(img)
    return filtered"""