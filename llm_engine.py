# llm_engine.py
import os
import numpy as np
from typing import Tuple

from tensorflow.keras.models import load_model

# Chemin du modèle entraîné
MODEL_PATH = os.path.join("models", "digit_cnn.h5")

# Chargement du modèle au démarrage
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Le modèle {MODEL_PATH} est introuvable. "
        f"Entraîne d'abord le modèle avec train_model.py."
    )

model = load_model(MODEL_PATH)


def predict_digit_from_pixels(pixels: np.ndarray) -> Tuple[int, float]:
    """
    Prend une image prétraitée (28x28, float32 entre 0 et 1)
    et renvoie (digit, confidence).

    pixels: np.ndarray shape (28, 28)
    """
    # S'assurer du bon type et de la bonne forme
    if pixels.shape != (28, 28):
        raise ValueError(f"pixels doit avoir la forme (28, 28), reçu {pixels.shape}")

    # Ajouter les dimensions batch et channel : (1, 28, 28, 1)
    x = pixels.reshape((1, 28, 28, 1))

    # Prédiction avec le modèle Keras
    probs = model.predict(x, verbose=0)[0]   # shape (10,)
    digit = int(np.argmax(probs))
    confidence = float(np.max(probs))

    return digit, confidence
