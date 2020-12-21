# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:30:20 2019

@author: Alec

"""
import cv2
import os
import numpy as np
#Create an object. 0 for external camera

class webCamSnapshotGenerator():
    
    #Adds a user to the training/test evaluation dataset
    def create_User(userName):
        #Replace with USERNAME variable from front end
        
        #Replace with new path or connect to a database
        trainpath = "C:\\Users\\gabri\\Documents\\445FaceRecognition\\training_data"
        testpath = "C:\\Users\\gabri\\Documents\\445FaceRecognition\\test_data"
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #Create 100 images
        #Every 5th image goes to test set for train test split 80/20 ratio
        for i in range(10):
            if i % 5 == 0:
                webcam = cv2.VideoCapture(0)
                check, frame = webcam.read()          
                print(check)
                print(type(frame))
                #Will Convert Image To GreyScale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor= 1.1,
                        minNeighbors= 5
                        )
                
                for (x, y, w, h) in faces:
                    r = max(w, h) / 2
                    centerx = x + w / 2
                    centery = y + h / 2
                    nx = int(centerx - r)
                    ny = int(centery - r)
                    nr = int(r * 2)

                faceimg = frame[ny:ny+nr, nx:nx+nr]
                cropped = cv2.resize(faceimg, (32, 32))
                
                if not os.path.exists(testpath):
                    os.makedirs(testpath)
                    cv2.imwrite(os.path.join(testpath, userName +' '+ str(i) + '.png'), img = cropped)
                    #Shut down the camera
                    
                else:
                    cv2.imwrite(os.path.join(testpath,userName +' '+ str(i) + '.png'), img = cropped)
                    #Shut down the camera
                    
            else:
                webcam = cv2.VideoCapture(0)
                check, frame = webcam.read()          
                print(check)
                print(frame)
                         #Will Convert Image To GreyScale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor= 1.1,
                        minNeighbors= 5
                        )
                print(len(faces))
                for (x, y, w, h) in faces:
                    r = max(w, h) / 2
                    centerx = x + w / 2
                    centery = y + h / 2
                    nx = int(centerx - r)
                    ny = int(centery - r)
                    nr = int(r * 2)

                faceimg = frame[ny:ny+nr, nx:nx+nr]
                cropped = cv2.resize(faceimg, (32, 32))
               
                
                
                if not os.path.exists(trainpath):
                    os.makedirs(trainpath)
                    cv2.imwrite(os.path.join(trainpath, userName + ' ' + str(i) + '.png'), img = cropped)
                    #Shut down the camera
                    
                else:
                    cv2.imwrite(os.path.join(trainpath, userName + ' ' + str(i) + '.png'), img = cropped)
                    #Shut down the camera
        webcam.release()
        print('Saved image')
  
    
   
    
    #User Requests to Login, Picture is taken added to set for prediction file
    def create_Prediction_Image():
        predictpath = "C:\\Users\\gabri\\Documents\\445FaceRecognition\\prediction_data"
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        webcam = cv2.VideoCapture(0)
        check, frame = webcam.read()          
        print(check)
        print(frame)
        
                #Will Convert Image To GreyScale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor= 1.1,
                minNeighbors= 5
                )
        print(len(faces))
        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)

        faceimg = frame[ny:ny+nr, nx:nx+nr]
        cropped = cv2.resize(faceimg, (32, 32))
        if not os.path.exists(predictpath):
            os.makedirs(predictpath)
            cv2.imwrite(os.path.join(predictpath, 'predict' + '.png'), img = cropped)
        else:
            cv2.imwrite(os.path.join(predictpath, 'predict' + '.png'), img = cropped)

        print('Saved image')
  
        #Shut down the camera
        webcam.release()
    
        
        
      
        
