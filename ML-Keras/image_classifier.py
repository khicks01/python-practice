from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm
from keras.datasets import cifar10 as cf10
import matplotlib.pyplot as plt
import keras.utils as utils
import numpy as np
from keras.optimizers import SGD

(train_images, train_labels), (test_images, test_labels) = cf10.load_data()

label_array = ['airplanes', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_labels = utils.to_categorical(train_labels)
test_labels = utils.to_categorical(test_labels)

train_images = train_images.astype('float32')

#normalize
train_images = train_images/255

test_images = test_images.astype('float32')

test_images = test_images/255

def reshape_image(input_image_arrays):
    output_array= []
    for image_array in input_image_arrays:
        output_array.append(image_array.reshape(-1))
    return np.asarray(output_array)

num_dimensions = 10
pic_size = 32


model = Sequential()
model.add(Conv2D(filters=pic_size, kernel_size=(3, 3), input_shape=(pic_size, pic_size, 3),
                 activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(MaxPooling2D(2, 2))
model.add(Flatten())
model.add(Dense(units=512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))
model.add(Dense(units=num_dimensions, activation='softmax'))

model.compile(optimizer=SGD(learning_rate=0.01), loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x=train_images, y=train_labels, epochs=1, batch_size=32)

model.save(filepath='C:\Git Repos\python-practice\ML-Keras\Image_Classifier.h5')
