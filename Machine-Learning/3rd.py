import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten ,Conv2D, MaxPooling2D
import pickle

X = pickle.load(open("x.pickle","rb"))
 
y = pickle.load(open("y.pickle","rb"))

X = X/255.0

model = Sequential()
# one layer
model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# two layer
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2))) 
# three layer 
model.add(Flatten())  
model.add(Dense(64))
# output layer
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.3)