# Traffic Sign Detection using CNN & Data Augmentation

This project focuses on Traffic Sign Detection using Convolutional Neural Networks (CNN) with an emphasis on data augmentation.

## Overview

- **Dataset:** [German Traffic Signs](https://bitbucket.org/jadslim/german-traffic-signs)
- **GitHub Repository:** [Traffic_Sign_Detection_CNN_Data_Augmentation](https://github.com/mrunmayee17/Traffic_Sign_Detection_CNN_Data_Augmentation.git)

## Setup and Dependencies

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/mrunmayee17/Traffic_Sign_Detection_CNN_Data_Augmentation.git

* 		Install the required libraries, including TensorFlow and Keras.
* 		Execute the provided Jupyter Notebook (main.ipynb) to run the project.
Key Steps
* 		Loading the Dataset: The project uses the German Traffic Signs dataset, which contains various traffic sign images. Reference file: utility/load_dataset.py 
* 		Data Preprocessing: Images are preprocessed by applying gray scaling and histogram equalization. Reference file: utility/preprocess_image.py 
* 		Data Augmentation: Data augmentation techniques are used to increase the size of the training dataset.
* 		Model Building: A Convolutional Neural Network (CNN) model is defined for traffic sign detection. Reference file: utility/load_model.py 
* 		Training: The CNN model is trained using the training dataset, with validation on a separate validation dataset.
* 		Evaluation: The model's performance is evaluated using test data, and metrics like accuracy and loss are plotted.
* 		Prediction: The trained model is used to predict traffic signs on sample images.
Results
* The project aims to improve road safety and traffic management by enhancing real-time traffic sign recognition.
* Various plots and visualizations are provided to understand the dataset and the model's performance.
* The accuracy of the model is evaluated on both the test dataset and custom traffic sign images.
References
* The project utilizes the German Traffic Signs dataset and various Python libraries, including TensorFlow and Keras.
* The code includes data preprocessing, data augmentation, model building, training, and evaluation steps for traffic sign detection.

