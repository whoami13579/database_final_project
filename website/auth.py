from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, login_required, logout_user
from .models import Teacher, Role
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        role_type = request.form.get("role_type")
        role_id = ord(role_type) - ord("0")

        if Teacher.query.filter_by(email=email).first():
            flash("Email is already in use.", category="error")
        elif len(password1) < 6:
            flash("Password should be at least 6 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match.", category="error")
        else:
            role = Role.query.filter_by(role_id=role_id).first()
            teacher = Teacher(email, name, generate_password_hash(password1), role_id)
            role.teachers.append(teacher)
            db.session.add(teacher)
            db.session.commit()

            login_user(teacher, remember=True)
            flash("Teacher created.", category="success")
            return redirect(url_for("views.home"))



    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        teacher = Teacher.query.filter_by(email=email).first()

        if teacher:
            if check_password_hash(teacher.password, password):
                flash("Logged in.", category="success")
                login_user(teacher, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password incorrect.", category="error")

        else:
            flash("User does not exist.", category="error")

    return render_template("login.html", user=current_user)
