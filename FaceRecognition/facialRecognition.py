# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:28:37 2019

@author: Alec
"""

# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
import dataPreprocessingLabel

import sys
sys.path.append('C:\\Users\\gabri\\Documents\\445FaceRecognition\\training_data')
sys.path.append('C:\\Users\\gabri\\Documents\\445FaceRecognition\\test_data')
sys.path.append('CC:\\Users\\gabri\\Documents\\445FaceRecognition\\prediction_data')

# Initialising the CNN
def buildNetwork():
    train_x_set, train_y_set = dataPreprocessingLabel.resize_Images('C:\\Users\\gabri\\Documents\\445FaceRecognition\\training_data') 
    ndim = len(list(set(np.array(train_y_set))))
    test_x_set, test_y_set = dataPreprocessingLabel.resize_Images('C:\\Users\\gabri\\Documents\\445FaceRecognition\\test_data')
    
    classifier = Sequential()
    # Step 1 - Convolution
    classifier.add(Conv2D(32, (3, 3), input_shape = (32,32, 3), activation = 'relu'))

    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    # Adding a second convolutional layer
    classifier.add(Conv2D(16, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    # Step 3 - Flattening
    classifier.add(Flatten())
    
    # Step 4 - Full connection
    classifier.add(Dense(units = 32, activation = 'relu'))
    classifier.add(Dense(units = ndim, activation = 'softmax'))
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy'])
    return classifier


print(dir(type(pd.DataFrame)))
    
    # Part 2 - Fitting the CNN to the images
def fit_evaluate_Model(classifier):
    train_x_set, train_y_set = dataPreprocessingLabel.resize_Images('C:\\Users\\gabri\\Documents\\445FaceRecognition\\training_data') 
    
    
    train_dataset = pd.DataFrame({'label': train_y_set, 'images': list(train_x_set)}, columns =['label','images'])

    
    test_x_set, test_y_set = dataPreprocessingLabel.resize_Images('C:\\Users\\gabri\\Documents\\445FaceRecognition\\test_data')    
    test_dataset = pd.DataFrame({'label': test_y_set, 'images': list(test_x_set)}, columns =['label','images'])

    
   
    train_datagen = ImageDataGenerator(rescale = 1./255,
                                      shear_range = 0.2,
                                      zoom_range = 0.2,
                                      horizontal_flip = True)
    valid_datagen = ImageDataGenerator(rescale = 1./255)
    test_datagen = ImageDataGenerator(rescale = 1./255) 
    train_generator = train_datagen.flow_from_dataframe(
            dataframe= train_dataset,
            directory= None,
            x_col= 'images',
            y_col='label',
            subset="training",
            batch_size = 2,
            seed = 42,
            shuffle = True,
            class_mode='categorical',
            target_size=(32,32))
    valid_generator = valid_datagen.flow_from_dataframe(
            dataframe= train_dataset,
            directory= None,
            x_col='images',
            y_col='label',
            subset="validation",
            batch_size = 5,
            seed = 42,
            shuffle = True,
            class_mode='categorical',
            target_size=(32,32))
    test_generator = test_datagen.flow_from_dataframe(
            dataframe= test_dataset,
            directory= None,
            x_col='images',
            y_col='label',
            batch_size = 1,
            seed = 42,
            shuffle = True,
            class_mode='categorical',
            target_size=(32,32))
    STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
    STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
    classifier.fit_generator(generator=train_generator,
                    steps_per_epoch=STEP_SIZE_TRAIN,
                    validation_data=valid_generator,
                    validation_steps=STEP_SIZE_TEST,
                    epochs=100)
    print(test_generator.classes)                
    classifier.evaluate_generator(generator= test_generator,steps= STEP_SIZE_TEST)
    

def predict():
    
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    classifier = model_from_json(loaded_model_json)
    classifier.load_weights("model.h5")
    
    predict_image = image.load_img('C:\\Users\\gabri\\Documents\\445FaceRecognition\\prediction_data\\predict.png')
    predict_image = image.img_to_array(predict_image)
    predict_image = predict_image.reshape(32,32,3)
    predict_image = np.expand_dims(predict_image, axis = 0)
    y_prediction = classifier.predict_classes(predict_image)
    train_x_set, train_y_set = dataPreprocessingLabel.resize_Images('C:\\Users\\gabri\\Documents\\445FaceRecognition\\training_data') 
    labels = np.unique(train_y_set)
    prediction = labels[y_prediction]
    return prediction
    
    #Serialize model to json and save
def serialize_Model(model):
    model_json = model.to_json()
    with open("model.json","w") as json_file:
        json_file.write(model_json)
    
    #Serialize weights
def serialize_Weights(model):
    model.save_weights("model.h5")
    print("Saved model to disk")
    
    
            