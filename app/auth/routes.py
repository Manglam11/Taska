from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from app import db, bcrypt
from app.models import User
from flask_login import login_user, logout_user, login_required
from app.auth import auth_bp

# auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    data = request.get_json()

    # Validate inputs
    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "").strip()

    if not name or not email or not password:
        return jsonify({"status": "error", "message": "All fields are required"}), 400

    if len(password) < 6:
        return jsonify({"status": "error", "message": "Password must be at least 6 characters"}), 400

    if User.query.filter_by(email=email).first():
            return jsonify({"status": "error", "message": "Email already registered"}), 400

    # Hash password and save
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(name=name, email=email, password_hash=hashed_pw)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"status": "success", "message": "Registration successful"}), 201

@auth_bp.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    data = request.get_json()

    email = data.get("email", "").strip().lower()
    password = data.get("password", "").strip()

    if not email or not password:
        return jsonify({"status": "error","message": "All fields are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"status": "error", "message": "Invalid email or password"}), 401

    login_user(user)
    return jsonify({"status": "success", "message": "Login successful"}), 200


@auth_bp.route("/auth/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))