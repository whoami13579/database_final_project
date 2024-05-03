from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

Reward_teacher = db.Table(
    "rewards_teachers",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column("reward_id", db.Integer, db.ForeignKey("rewards.reward_id")),
)


class Role(db.Model):
    __tablename__ = "roles"

    def __init__(self, role_id, name):
        self.role_id = role_id
        self.role_name = name

    role_id = db.Column(db.Integer, primary_key=True)
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

    schedule_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer)
    time = db.Column(db.Integer)
    name = db.Column(db.String(20))

    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="class_schedules")

    def __repr__(self):
        return f"id: {self.id}, week: {self.week}, time: {self.time}, name: {self.name}"


class Teacher(db.Model, UserMixin):
    __tablename__ = "teachers"

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    teacher_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(150))
    self_introduction = db.Column(db.String(500), nullable=True)
    photo_path = db.Column(db.String(150), nullable=True)
    offict_phone = db.Column(db.String(10), nullable=True)
    personal_website = db.Column(db.String(150), nullable=True)
    interest = db.Column(db.String(150), nullable=True)

    role_id = db.Column(db.ForeignKey("roles.role_id"))

    def __repr__(self):
        return f"id: {self.id}, email: {self.email}, name: {self.name}"


class Reward(db.Model):  # Reward_and_guide_students_to_win_wards
    __tablename__ = "rewards"

    def __init__(self, id, time, award, school, attribute, name):
        self.reward_id = id
        self.reward_time = time
        self.award = award
        self.school = school
        self.attribute = attribute
        self.name = name

    reward_id = db.Column(db.Integer, primary_key=True)
    reward_time = db.Column(db.Date)
    award = db.Column(db.String(50))
    school = db.Column(db.String(50))
    attribute = db.Column(db.String(50))
    name = db.Column(db.String(50))

    teacher = db.relationship("Teacher", secondary=Reward_teacher, backref="rewards")

    def __repr__(self):
        return f"id: {self.reward_id}, time: {self.reward_time}, award: {self.award}, school: {self.school}, attribute: {self.attribute}, name: {self.name}"

