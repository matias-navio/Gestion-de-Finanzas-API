from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config  # Importa la configuración

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Carga la configuración

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Importar los modelos aquí para evitar problemas de importación circular
    from models.models import Income, Expense

    @app.route('/')
    def home():
        return "Base de datos y tablas creadas exitosamente."

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
