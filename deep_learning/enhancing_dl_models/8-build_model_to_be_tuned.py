#!/usr/bin/env python3
"""Enhancing Deep Learning Models
"""

from tensorflow import keras


def build_model(hp):
    '''build model'''    
    model = keras.Sequential()
    model.add(keras.layers.InputLayer(input_shape=(784,)))

    for i in range(hp.Int('num_layers', min_value=1, max_value=2)):
        model.add(keras.layers.Dense(
            units=hp.Int('units', min_value=4, max_value=12, step=4),
            activation=hp.Choice('activation', values=['relu', 'sigmoid'])
        ))

    model.add(keras.layers.Dense(10, activation='softmax'))

    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=hp.Choice('learning_rate', values=[1e-2, 1e-3])
        ),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
