# api/routes_digit.py
from flask import Blueprint, request, jsonify
from PIL import Image
import numpy as np

from llm_engine import predict_digit_from_pixels

digit_api = Blueprint("digit_api", __name__)


@digit_api.post("/digit_classification")
def digit_classification():
    """
    Classifier un chiffre manuscrit à partir d'une image
    ---
    tags:
      - Digit Classification
    consumes:
      - multipart/form-data
    parameters:
      - name: image
        in: formData
        type: file
        required: true
        description: Image contenant un seul chiffre manuscrit (0-9).
    responses:
      200:
        description: Résultat de la classification
        schema:
          type: object
          properties:
            digit:
              type: integer
              example: 7
            confidence:
              type: number
              format: float
              example: 0.93
      400:
        description: Erreur de requête (image manquante ou invalide)
      500:
        description: Erreur interne côté serveur / modèle
    """
    # Vérifie qu'un fichier "image" est bien présent
    if "image" not in request.files:
        return jsonify({"error": "Aucun fichier 'image' dans la requête"}), 400

    file_storage = request.files["image"]

    if file_storage.filename == "":
        return jsonify({"error": "Nom de fichier vide"}), 400

    try:
        img = Image.open(file_storage.stream).convert("L")
        img = img.resize((28, 28))

        # Normalisation
        pixels = np.array(img, dtype=np.float32) / 255.0

        # ⚠️ INVERSION : si ton chiffre est noir sur fond blanc,
        # on le transforme en blanc sur fond noir comme MNIST
        pixels = 1.0 - pixels

        # Appel au moteur IA (LLM / modèle vision léger)
        digit, confidence = predict_digit_from_pixels(pixels)

        return jsonify(
            {
                "digit": int(digit),
                "confidence": float(confidence),
            }
        ), 200

    except Exception as e:
        # En prod, tu logguerais l'erreur au lieu de l'afficher directement
        return jsonify({"error": f"Erreur lors du traitement de l'image : {str(e)}"}), 500

