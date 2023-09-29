import streamlit as st
import pandas as pd
import numpy as np #for computations
import pandas as pd #to read the data
import seaborn as sns #for visualization
import matplotlib.pyplot as plt #for visualization
import cv2 #for image manipulation
import os
from PIL import Image
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model


#define a pipeline for preprocessing
def image_preprocessing(image, ksize=(3,3), dsize=(32,32)):
  """
  preprocesses the image by reducing the size and implementing gaussianblur
  image: images from the dataset
  ksize: (Tuple)kernel size for gaussianblur
  dsize: (Tuple) size of the image
  """
  img_np = np.array(image) #first convert the image to numpy array
  #resize the images and store it in the resize list
  resized_image = cv2.resize(img_np, dsize=dsize, interpolation=cv2.INTER_AREA)
  
  #blur the images
  blur_image = cv2.GaussianBlur(resized_image, ksize=ksize, sigmaX=0)

  # Normalizing the image pixels
  image_normalized = np.array(blur_image).astype('float32')/255.0

  #expand dimension
  image_prep = np.expand_dims(a=image_normalized,axis=0)

  return image_prep

#create a title for the App
st.title('Covid19 Predictor Application')
st.write('Kindly upload an X-ray image an we will predict if you have contracted Covid19, Viral Pneumonia, or you are completely healthy')

# #load the trained model
model_pb = load_model('/Users/user/Documents/MLOps/covid_project/cov_model')
model = tf.keras.models.clone_model(model_pb)
    
# #load the encoder
lb_path = '/Users/user/Documents/MLOps/covid_project/label_binarizer.pkl'
with open(lb_path, mode='rb') as lb:
    lb = pickle.load(lb)

#create file uploader so the user can upload an image
uploaded_image = st.file_uploader('Upload an Image', type=None)
button = st.button(label='Make Prediction')

#if user has uploaded a file, display the image
if uploaded_image is not None and button:
    img = Image.open(uploaded_image)
    st.image(img, caption=['uploaded image'] )
    # #preprocess the image
    image_prep = image_preprocessing(img)

        
    # #make prediciton using the model
    pred = model.predict(image_prep)

    # #get the label of the pred
    #label = np.argmax(pred)

    category = lb.inverse_transform(pred)
    st.write(f'## The category is predicted to be: {category}')