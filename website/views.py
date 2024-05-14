from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Role, Teacher
from . import db
from datetime import datetime

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", user=current_user, teachers=Teacher.query.all())


@views.route("/role/<role_id>")
def role(role_id):
    return render_template("role.html", user=current_user, teachers=Teacher.query.filter_by(role_id=role_id), role=Role.query.filter_by(role_id=role_id).first())
