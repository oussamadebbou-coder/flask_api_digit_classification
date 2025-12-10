# app.py
from flask import Flask
from flasgger import Swagger
from api.routes_digit import digit_api

def create_app():
    app = Flask(__name__)

    # Configuration minimale de Swagger
    app.config["SWAGGER"] = {
        "title": "Digit Classification API",
        "uiversion": 3,
    }

    Swagger(app)  # instancie Swagger

    # Enregistrement du blueprint pour les routes de classification
    app.register_blueprint(digit_api, url_prefix="/api")

    return app


if __name__ == "__main__":
    app = create_app()
    # debug=True pour le développement uniquement
    app.run(debug=True)
