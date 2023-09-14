import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from keras.layers import Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D

def modified_model():
  model = Sequential()

# prarameters to adjust = 30*5*5+30 = 780
  model.add(Conv2D(60, (5,5), input_shape = (32,32,1), activation='relu'))
  model.add(Conv2D(60, (5,5), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2,2)))

  model.add(Conv2D(30, (3,3),activation='relu'))
  model.add(Conv2D(30, (3,3),activation='relu'))
  model.add(MaxPooling2D(pool_size=(2,2)))

  # model.add(Dropout(0.5))
  model.add(Flatten())

  model.add(Dense(units = 500, activation = 'relu'))
  model.add(Dropout(0.5))
  model.add(Dense(units = 43, activation = 'softmax'))
  #optimizer
  adam = Adam(lr = 0.001)

  model.compile(adam, loss = keras.losses.CategoricalCrossentropy(), metrics = ['accuracy'])
  return model