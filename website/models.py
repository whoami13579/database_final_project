from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy


class Role(db.Model):
    __tablename__ = "roles"

    def __init__(self, type, name):
        self.role_type = type
        self.role_name = name

    # id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, primary_key=True)
    # role_type = db.Column(db.Integer, unique=True)
    role_name = db.Column(db.String(20), unique=True)

    teachers = db.relationship("Teacher", backref="role")

    def __repr__(self):
        return f"id: {id}, role_ytpe: {self.role_type}, role_name{self.role_name}"


class Class_schedule(db.Model):
    __tablename__ = "class_schedule"

    def __init__(self, week, time, name):
        self.week = week
        self.time = time
        self.name = name

    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer)
    time = db.Column(db.Integer)
    name = db.Column(db.String(20))

    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    def __repr__(self):
        return f"id: {self.id}, week: {self.week}, time: {self.time}, name: {self.name}"


class Teacher(db.Model, UserMixin):
    __tablename__ = "teachers"

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    teacher_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    self_introduction = db.Column(db.String(500), nullable=True)

    role_id = db.Column(db.ForeignKey("roles.role_id"))

    class_schedules = db.relationship("Class_schedule", backref="teacher")

    def __repr__(self):
        return f"id: {self.id}, email: {self.email}, name: {self.name}"
