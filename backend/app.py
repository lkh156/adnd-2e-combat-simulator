from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adnd2e.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Home route
@app.route('/')
def home():
    return "AD&D 2E API is running!"

# Run the app
if __name__ == '__main__':
    # Use the application context to create the database
    with app.app_context():
        if not os.path.exists('adnd2e.db'):
            db.create_all()  # Create the database if it doesn't exist
    app.run(debug=True)
