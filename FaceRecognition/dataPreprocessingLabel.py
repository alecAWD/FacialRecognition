# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:23:08 2019

@author: Alec
"""
import re
import os
import PIL
from PIL import Image

from io import BytesIO
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
    #Resizes Images in Folder
def resize_Images(folder):
    #Image Array
    images = []
    resizedImages = []
    usernames = []
    basewidth = 64
    #For each file in folder
    for filename in os.listdir(folder):
        #Open the image file from the folder
        img = load_img(os.path.join(folder,filename))
        parsedFilePath = re.findall(r'\w+', img.filename)
    #Find the username in the file path
        username = parsedFilePath[8]
        usernames.append(username)        
        
        #imgArray = imgArray.reshape((1,) + imgArray.shape)
        resizedImages.append(img.filename)

    return resizedImages, usernames
    
       
    

    
            
