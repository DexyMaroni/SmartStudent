# app/auth/routes.py
from flask import Blueprint, request, jsonify
from app import db
from app.auth.models import User
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint for user login.

    This route handles the POST request to authenticate a user. It expects a JSON payload with the following fields:
    - username: The username of the user.
    - password: The password of the user.

    The function retrieves the user from the database based on the provided username. If the user exists and the password
    is correct, the user is logged in and a JSON response with the message "Logged in successfully" and the status code 200
    is returned. If the user does not exist or the password is incorrect, a JSON response with the message "Invalid
    credentials" and the status code 401 is returned.

    Parameters:
    None

    Returns:
    - If the login is successful:
        - A JSON response with the message "Logged in successfully" and the status code 200.
    - If the login is unsuccessful:
        - A JSON response with the message "Invalid credentials" and the status code 401.
    """
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify(message="Logged in successfully"), 200
    return jsonify(message="Invalid credentials"), 401

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    data = request.get_json()
    logout_user()
    return jsonify(message="Logged out successfully"), 200
