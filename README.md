# Driver-Drowsiness-Detection
Drowsy driving is the dangerous combination of driving when sleepy. This usually happens when a driver has not slept enough, but it can also happen because of untreated sleep disorders or shift work. Prescription and over-the-counter medications can also cause drowsiness, and alcohol can interact with sleepiness to increase both impairment and drowsiness.

This ML Model Detects a Drowsy Driver, and alet them about the danger.

## Accuracy
Validation Accuracy = 0.9225 (92%).
Data Set Of 48K images.

## Dataset

This dataset is just one part of The MRL Eye Dataset, Our dataset includes 24K images for both closed and open eye categories.

Training images : 38400

Validation images : 9600

Dataset has been already balanced,i.e both categories have same num of images. Thus, we shall only look at Accuracy metric.

Key metric to consider model performance -> val_categorical_accuracy.

## Limitation
Model have a set value of drowsyness scale at 23, when actual Score should be 13.
This is because dataset of eyes with spectacles is have less dataset which tend to give "Not so good Results" when score =13.

## ConvNet Model 
A convolutional neural network can have tens or hundreds of layers that each learn to detect different features of an image. Filters are applied to each training image at different resolutions, and the output of each convolved image is used as the input to the next layer. The filters can start as very simple features, such as brightness and edges, and increase in complexity to features that uniquely define the object.

![1669126552865](https://user-images.githubusercontent.com/98209563/218676958-e067a25b-2725-423a-8b91-c8b3292d4c70.jpg)

Consider using CNNs when you have a large amount of complex data (such as image data). You can also use CNNs with signal or time-series data when preprocessed to work with the network structure.
![1669126552882](https://user-images.githubusercontent.com/98209563/218677107-7294702c-b299-4617-aa16-bafd575a767b.jpg)


Model: "sequential"
![pipeline](https://user-images.githubusercontent.com/98209563/224373565-7de14913-f9e4-4c5e-b54c-39c24ea6c762.png)


No, of layers: 10

![image](https://user-images.githubusercontent.com/98209563/218672729-54f64a92-ad61-409d-97d0-51bc7a75ea79.png)

![image](https://user-images.githubusercontent.com/98209563/218673254-b2f459c1-51f0-4fef-82db-0743b9f71842.png)

## Model Accuracy

![download](https://user-images.githubusercontent.com/98209563/218671951-c3dfb2f4-06a3-4e28-9d90-0a8d44d103fc.png)
## Model Loss

![download](https://user-images.githubusercontent.com/98209563/218672006-1b8f9b4a-b096-42a5-9ff5-77f4938d6427.png)

