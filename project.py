import cv2
import pytesseract

# referenee to our executable file so we us this below
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# to read image
img=cv2.imread('9.png')
                # path
# the thing with pytesseract is that it only accept RGB values while opencv
# in BGR so first we will convert before sending
# it to pytesseract library
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# it will convert the given image to string
print(pytesseract.image_to_string(img))

# it will give the details of each letters like
# x axis y axis width and height which in actual diagonal points




# Detecting characters by characters
# print(pytesseract.image_to_boxes(img))
# hImg,wImg,_=img.shape
# boxes =pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     # print(b) # we will be getting the same info as above
#     b=b.split(' ')# convert all the elemnets to list
#     print(b)
#     x,y,w,h=int (b[1]),int (b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,225),3)
#     # if they were detected properly or not
#     #  to detect word by word
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
#
# # # after conversion we can display
# cv2.imshow('Result',img)
#
# # # used to delay the image
# cv2.waitKey(0)



# ## DETECTING  words
# hImg,wImg,_=img.shape
# boxes =pytesseract.image_to_data(img)
# # print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     # print(b) # we will be getting the same info as above
#     if x!=0:
#         b=b.split()# convert all the elemnets to list
#         #print(b)
#         if len(b)==12:
#             x,y,w,h=int (b[6]),int (b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,225),3)
#             # if they were detected properly or not
#             #  to detect word by word
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
# # after conversion we can display
# cv2.imshow('Result',img)
#
# # used to delay the image
# cv2.waitKey(0)


### DETECTING  Digits
hImg,wImg,_=img.shape
cong=r'--oem 3 --psm 6 outputbase  digits'
# --psm controls the automatic Page Segmentation Mode
# here 6 is single uniform block of text by default
boxes =pytesseract.image_to_data(img,config=cong)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    # print(b) # we will be getting the same info as above
    if x!=0:
        b=b.split()# convert all the elemnets to list
        print(b)
        if len(b)==12:
            x,y,w,h=int (b[6]),int (b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,225),3)
            # if they were detected properly or not
            #  to detect word by word
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
# after conversion we can display
cv2.imshow('Result',img)

# used to delay the image
cv2.waitKey(0)
