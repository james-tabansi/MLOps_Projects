# James Chukwuka Tabansi
# Background and Context
- Covid-19 is a fast-growing disease that affects human health severely. Patients diagnosed with this condition suffer from lung infections. The medical community has recently released vaccines that have a slower effect in increasing immunity. This virus has impacted various countries\' human health and financial standards.

- Deep learning algorithms have recently used image classification to identify medical images. Convolutional Neural Networks (CNN) can be widely utilized to identify COVID-19 to assist radiologists in medical analysis by classifying patients who are healthy, have viral pneumonia, or are affected by COVID using X-ray pictures of the lungs.

# Objective
- The aim of this project is two folds:

  - Build a deep learning model  to differentiate an X-ray image of a normal person from an unhealthy one.
  - Build an app using Streamlit for users to make predictions or inference using your model.

# Data Description
- This dataset contains training set images of 3 classes which are converted into numpy arrays.
- The dataset comprises 3 classes:
  - COVID-19: The patient who is affected due to covid.
  - Viral Pneumonia: This is a viral fever that has similar characteristics to Covid but is not covid.
  - Normal- A healthy Person.
- The data file names are:
  - CovidImages.npy
  - CovidLabels.csv
- Due to the large volume of data, the images were converted to the CovidImages.npy file and the labels are also put into CovidLabels.csv so that you can work on the data/project seamlessly without having to worry about the high data volume.

## Metric to optimize
- the following metrics will be considered
  - 1. ROC-AUC (on a 1-vs-all basis, since this is multi-label classification)
  - 2. Categorical Accuracy



