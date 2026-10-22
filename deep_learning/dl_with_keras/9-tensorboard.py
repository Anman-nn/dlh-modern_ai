#!/usr/bin/env python3
"""Introduction to Deep Learning with Keras Project
"""

from tensorflow import keras
import datetime


def log_to_tensorboard(log_dir, model, X, Y, epochs, verbose=1):
    """
    log_to_tensorboard
    """

    log_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = f"{log_dir}/{log_name}"
    cb = keras.callbacks.TensorBoard(
        log_dir=path,
        histogram_freq=1,
        update_freq='epoch'
    )

    model.fit(X, Y, epochs=epochs, verbose=verbose, callbacks=[cb])

    return None
