from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D


def fully_connected(input_shape, output_dim):
    model = Sequential()
    # 1st Convolution Layer
    model.add(Conv2D(filters=96, input_shape=input_shape, kernel_size=(11, 11), strides=(4, 4), padding="valid"))
    model.add(Activation("relu"))
    # Max Pooling
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
    # # Passing it to a Fully Connected layer
    model.add(Flatten())
    # 1st Fully Connected Layer
    model.add(Dense(1024))
    model.add(Activation("relu"))
    # Add Dropout to prevent over-fitting
    model.add(Dropout(0.4))

    model.add(Dense(output_dim))
    model.add(Activation("softmax"))

    return model

