from keras.datasets import cifar10 as cf10
import matplotlib.pyplot as plt
import keras.utils as utils
import numpy as np

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

