from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

Reward_teacher = db.Table(
    "rewards_teachers",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column("reward_id", db.Integer, db.ForeignKey("rewards.reward_id")),
)

JournalArtical_teacher = db.Table(
    "journalArtical_teachers",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "journal_artical_id",
        db.Integer,
        db.ForeignKey("journal_articals.journal_artical_id"),
    ),
)

TeachingMaterialsAndWorks_teacher = db.Table(
    "TeachingMaterialsAndWorks_teacher",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "teaching_materials_and_works_id",
        db.Integer,
        db.ForeignKey("TeachingMaterialsAndWorks.teaching_materials_and_works_id"),
    ),
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


# Reward_and_guide_students_to_win_wards
class Reward(db.Model):
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


# Approved_patents
class Patent(db.Model):
    __tablename__ = "patents"

    def __init__(self, name, date, number, patent_type, teacher_id):
        self.patent_name = name
        self.date = date
        self.number = number
        self.patent_type = patent_type
        self.teacher_id = teacher_id

    patent_id = db.Column(db.Integer, primary_key=True)
    patent_name = db.Column(db.String(150))
    date = db.Column(db.Date)
    number = db.Column(db.Integer)
    patent_type = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="patents")

    def __repr__(self):
        return f"id: {self.patent_id}, name: {self.patent_name}, date: {self.date}, number: {self.number}, type: {self.patent_type}, teacher_id: {self.teacher_id}"


class InternalExperience(db.Model):
    __tablename__ = "internal_experiences"

    def __init__(self, department, teacher_id):
        self.department = department
        self.teacher_id = teacher_id

    internal_experience_id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="internal_experiencs")

    def __repr__(self):
        return f"id: {self.internal_experience_id}, department: {self.department}, teacher_id: {self.teacher_id}"


class ExternalExperience(db.Model):
    __tablename__ = "external_experiences"

    def __init__(self, date, school, department, position, teacher_id):
        self.date = date
        self.school = school
        self.department = department
        self.position = position
        self.teacher_id = teacher_id

    external_experience_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    school = db.Column(db.String(50))
    department = db.Column(db.String(50))
    position = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="external_experiences")

    def __repr__(self):
        return f"id: {self.external_experience_id}, date: {self.date}, school: {self.school}, department: {self.department}, position: {self.position}, teacher_id: {self.teacher_id}"


class JournalArtical(db.Model):
    __tablename__ = "journal_articals"

    def __init__(
        self,
        course_name,
        journal_name,
        collaborators,
        page_number_of_the_journal,
        indexed_website,
        indexed_time,
    ):
        self.course_name = course_name
        self.journal_name = journal_name
        self.collaborators = collaborators
        self.page_number_of_the_journal = page_number_of_the_journal
        self.indexed_website = indexed_website
        self.indexed_time = indexed_time

    journal_artical_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50))
    journal_name = db.Column(db.String(50))
    collaborators = db.Column(db.String(50))
    page_number_of_the_journal = db.Column(db.Integer)
    indexed_website = db.Column(db.String(150))
    indexed_time = db.Column(db.Date)

    teachers = db.relationship(
        "Teacher", secondary=JournalArtical_teacher, backref="journal_articals"
    )

    def __repr__(self):
        return f"id: {self.journal_artical_id}, course name: {self.course_name}, journal name: {self.journal_name}, collaborators: {self.collaborators}, page number of the journal: {self.page_number_of_the_journal}, indexed website: {self.indexed_website}, indexed time: {self.indexed_time}"


class TeachingMaterialsAndWorks(db.Model):
    __tablename__ = "teaching_materials_and_works"

    def __init__(self, publisher, name, authros, teaching_materials_and_works_type):
        self.publisher = publisher
        self.name = name
        self.authors = authros
        self.teaching_materials_and_works_type = teaching_materials_and_works_type

    teaching_materials_and_works_id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(50))
    name = db.Column(db.String(50))
    authors = db.Column(db.String(150))
    teaching_materials_and_works_type = db.Column(db.String(50))

    teachers = db.relationship(
        "Teacher",
        secondary=TeachingMaterialsAndWorks_teacher,
        backref="teaching_materials_and_works",
    )

    def __repr__(self):
        return f"id: {self.teaching_materials_and_works_id}, publisher: {self.publisher}, name: {self.name}, authors: {self.authors}, type: {self.teaching_materials_and_works_type}"
