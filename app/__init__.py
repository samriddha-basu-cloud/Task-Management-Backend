from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///tasks.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize CORS with specific origins
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "https://task-management-application-by-basu.vercel.app/"]}})

    db.init_app(app)

    # Import routes here to avoid circular imports
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
