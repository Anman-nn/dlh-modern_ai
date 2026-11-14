#!/usr/bin/env python3
"""Computer Vision Architectures
"""

from tensorflow import keras


def compile_and_train_cnn(
    model, epochs, batch_size, x_train,
    y_train, x_val, y_val, optimizer_name='adam',
    optimizer_params=None
    ):
    '''compile_and_train_cnn'''
    if optimizer_name == 'adam':
        optimizer = keras.optimizers.Adam(
            learning_rate=optimizer_params.get('learning_rate', 0.001)
        )
    elif optimizer_name == 'SGD':
        optimizer = keras.optimizers.SGD(
            learning_rate=optimizer_params.get('learning_rate', 0.01)
        )
    elif optimizer_name == 'RMSprop':
        optimizer = keras.optimizers.RMSprop(
            learning_rate=optimizer_params.get('learning_rate', 0.001)
        )

    model.compile(
        optimizer=optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    history = model.fit(
        x_train,
        y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2
    )

    return model, history
