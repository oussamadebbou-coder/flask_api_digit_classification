# train_model.py
import os

import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
)
from tensorflow.keras.utils import to_categorical

# Dossier de sortie du modèle
os.makedirs("models", exist_ok=True)
MODEL_PATH = os.path.join("models", "digit_cnn.h5")


def build_model(input_shape=(28, 28, 1), num_classes=10):
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation="relu"),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dropout(0.5),
        Dense(num_classes, activation="softmax"),
    ])

    model.compile(
        loss="categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"],
    )
    return model


def main():
    # Chargement du dataset MNIST
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalisation et ajout du channel
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    x_train = np.expand_dims(x_train, -1)  # (N, 28, 28, 1)
    x_test = np.expand_dims(x_test, -1)

    # One-hot encoding des labels
    y_train_cat = to_categorical(y_train, 10)
    y_test_cat = to_categorical(y_test, 10)

    # Construction du modèle
    model = build_model()

    # Entraînement
    model.fit(
        x_train,
        y_train_cat,
        epochs=5,
        batch_size=128,
        validation_data=(x_test, y_test_cat),
    )

    # Évaluation rapide
    loss, acc = model.evaluate(x_test, y_test_cat, verbose=0)
    print(f"Accuracy sur MNIST : {acc:.4f}")

    # Sauvegarde du modèle
    model.save(MODEL_PATH)
    print(f"Modèle sauvegardé dans : {MODEL_PATH}")


if __name__ == "__main__":
    main()
