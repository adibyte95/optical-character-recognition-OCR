
# coding: utf-8

# In[2]:


# importing the dependencies
import os
import os.path
import cv2
import glob
import imutils


# In[53]:


# a function to take a path to an image and then segments the image into constituent letters and then return the letter

def image_segmentation(image_name):
    counter = 0
    # reading the image
    image = cv2.imread(image_name)

    # converting the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold to convert the image to pure black and white
    thresh = cv2.threshold(gray, 0,255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


    # find the contours (continous blob of pixels ) in the image 
    contours = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Hack for compatibility with different OpenCV versions
    contours = contours[0] if imutils.is_cv2() else contours[1]

    letter_image_regions = []

    # now loop through each of the letter in the image 
    for contour in contours:
        # get the rectangle that contains the contour
        x,y,w,h = cv2.boundingRect(contour)
        # compare the width and height of the contour to detect if it
        # has one letter or not
        if w/h >1.25:
            # this is too wide for a single letter
            continue
        elif w<3 or h<3:
            # this is a very small image probably a noise
            continue
        else:
        # this is a normal letter by itself
            letter_image_regions.append((x,y,w,h))

        # Extract the letter from the original image with a 2-pixel margin around the edge
        letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]
        #constructing the name of the images 
        name = str(counter) + '.png'
        # incrementing the counter to store the next image 
        counter = counter +1
        return letter_image


# In[58]:


letter_images = image_segmentation("pic.jpg")

