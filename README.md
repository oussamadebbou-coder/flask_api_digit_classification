
# 🧠 Digit Classification API (Flask + CNN)

Une API capable de reconnaître un chiffre manuscrit (0–9) à partir d’une image.  
Elle utilise **Flask**, **Swagger** (Flasgger) et un **modèle CNN entraîné sur MNIST**.

---

## 📌 Fonctionnalités

- 🔍 Route POST `/api/digit_classification`  
- 📤 Upload d’une image via `multipart/form-data`
- 🧼 Prétraitement automatique :  
  - grayscale  
  - resize 28×28  
  - normalisation  
  - inversion noir/blanc (compatible MNIST)
- 🤖 Modèle CNN (**digit_cnn.h5**) pour classifier les chiffres
- 📘 Documentation Swagger disponible sur `/apidocs`
- 🛠 Code structuré (Blueprint + moteur IA séparé)

---

## 📁 Structure du projet

```
digit-classification/
│
├── app.py
├── llm_engine.py
├── requirements.txt
│
├── models/
│   └── digit_cnn.h5
│
├── api/
│   ├── __init__.py
│   └── routes_digit.py
│
└── static/
    └── swagger_digit.json (optionnel)
```

---

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/<ton_repo>/digit-classification.git
cd digit-classification
```

### 2. Créer un environnement virtuel
```bash
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## 🤖 Entraîner le modèle (facultatif)

Le script `train_model.py` permet de générer :

```
models/digit_cnn.h5
```

---

## ▶️ Lancer l’API

```bash
python app.py
```

Swagger sera disponible ici :

👉 http://localhost:5000/apidocs

---

## 📤 Exemple d'appel API avec curl

```bash
curl -X POST http://localhost:5000/api/digit_classification   -F "image=@digit.png"
```

---

## 🧪 Exemple Postman

1. Méthode : **POST**  
2. URL : `http://localhost:5000/api/digit_classification`
3. Body → **form-data**
4. Ajouter une clé :

| KEY   | VALUE     | TYPE |
|-------|-----------|------|
| image | digit.png | File |

---

## 🧠 Fonctionnement interne

- Image convertie en niveaux de gris  
- Redimensionnée 28×28  
- Normalisée entre 0 et 1  
- Inversée (1 - pixels)  
- Envoyée au modèle CNN  
- Retour JSON :

```json
{
  "digit": 3,
  "confidence": 0.982
}
```

---

## 🏗️ Technologies utilisées

- Python 3  
- Flask  
- Flasgger (Swagger UI)  
- TensorFlow / Keras  
- NumPy  
- Pillow  

---

## 📜 Licence

Projet libre d’utilisation à des fins éducatives ou personnelles.

---

## ✨ Auteur

Oussama Debbou – 2025  
N'hésite pas à contribuer !

