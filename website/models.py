from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy


JournalArtical_teacher = db.Table(
    "journalArtical_teachers",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "journal_artical_id",
        db.Integer,
        db.ForeignKey("journal_articals.journal_artical_id"),
    ),
)

TeachingWork_teacher = db.Table(
    "teachingWork_teacher",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "teaching_work_id",
        db.Integer,
        db.ForeignKey("teaching_works.teaching_work_id"),
    ),
)

ProceedingArtical_teacher = db.Table(
    "proceedingArtical_teacher",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "proceeding_artical_id",
        db.Integer,
        db.ForeignKey("proceeding_articals.proceeding_artical_id"),
    ),
)

BookChapter_teacher = db.Table(
    "bookChapter_teacher",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "book_chapter_id",
        db.Integer,
        db.ForeignKey("book_chapters.book_chapter_id"),
    ),
)

BookReport_teacher = db.Table(
    "bookReport_teacher",
    db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.teacher_id")),
    db.Column(
        "book_report_id",
        db.Integer,
        db.ForeignKey("book_reports.book_report_id"),
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


class ClassSchedule(db.Model):
    __tablename__ = "class_schedule"

    def __init__(self, week, time, name, teacher_id):
        self.week = week
        self.time = time
        self.name = name
        self.teacher_id = teacher_id

    schedule_id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer)
    time = db.Column(db.Integer)
    name = db.Column(db.String(20))
   
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="class_schedules")

    def __repr__(self):
        return f"id: {self.schedule_id}, week: {self.week}, time: {self.time}, name: {self.name}, teacher_id: {self.teacher_id}"



class Teacher(db.Model, UserMixin):
    __tablename__ = "teachers"

    def __init__(self, email, name, password, role_id):
        self.email = email
        self.name = name
        self.password = password
        self.role_id = role_id
        self.self_introduction = ""
    
    def get_id(self):
        return (self.teacher_id)

    teacher_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(150))
    self_introduction = db.Column(db.String(500), nullable=True)
    photo_path = db.Column(db.String(150), nullable=True)
    offict_phone = db.Column(db.String(10), nullable=True)
    personal_website = db.Column(db.String(150), nullable=True)
    interest = db.Column(db.String(150), nullable=True)
    school = db.Column(db.String(150), nullable=True)

    role_id = db.Column(db.ForeignKey("roles.role_id"))

    def __repr__(self):
        return f"id: {self.teacher_id}, email: {self.email}, name: {self.name}"


# Reward_and_guide_students_to_win_wards
class Reward(db.Model):
    __tablename__ = "rewards"

    def __init__(self, time, award, school, attribute, name, teacher_id):
        self.reward_time = time
        self.award = award
        self.school = school
        self.attribute = attribute
        self.name = name
        self.teacher_id = teacher_id

    reward_id = db.Column(db.Integer, primary_key=True)
    reward_time = db.Column(db.Date)
    award = db.Column(db.String(50))
    school = db.Column(db.String(50))
    attribute = db.Column(db.String(50))
    name = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="rewards")

    def __repr__(self):
        return f"id: {self.reward_id}, time: {self.reward_time}, award: {self.award}, school: {self.school}, attribute: {self.attribute}, name: {self.name}, teacher_id: {self.teacher_id}"


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
    number = db.Column(db.String(50))
    patent_type = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="patents")

    def __repr__(self):
        return f"id: {self.patent_id}, name: {self.patent_name}, date: {self.date}, number: {self.number}, type: {self.patent_type}, teacher_id: {self.teacher_id}"

class InternalExperience(db.Model):
    __tablename__ = "internal_experiences"

    def __init__(self, department, position, teacher_id):
        self.department = department
        self.position = position
        self.teacher_id = teacher_id

    internal_experience_id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50))
    position = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="internal_experiencs")

    def __repr__(self):
        return f"id: {self.internal_experience_id}, department: {self.department}, position: {self.position}, teacher_id: {self.teacher_id}"



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
    page_number_of_the_journal = db.Column(db.String(50))
    indexed_website = db.Column(db.String(150))
    indexed_time = db.Column(db.Date)

    teachers = db.relationship(
        "Teacher", secondary=JournalArtical_teacher, backref="journal_articals"
    )

    def __repr__(self):
        return f"id: {self.journal_artical_id}, course name: {self.course_name}, journal name: {self.journal_name}, collaborators: {self.collaborators}, page number of the journal: {self.page_number_of_the_journal}, indexed website: {self.indexed_website}, indexed time: {self.indexed_time}"

    def compare(self, other):
        if self.course_name != other.course_name:
            return False
        if self.journal_name != other.journal_name:
            return False
        if self.collaborators != other.collaborators:
            return False
        if self.page_number_of_the_journal != other.page_number_of_the_journal:
            return False
        if self.indexed_website != other.indexed_website:
            return False
        if self.indexed_time != other.indexed_time:
            return False
        return True

    def to_dict(self):
        return {field.name:getattr(self, field.name) for field in self.__table__.c}


# teaching_materials_and_works
class TeachingWork(db.Model):
    __tablename__ = "teaching_works"

    def __init__(self, publisher, name, authros, teaching_work_type):
        self.publisher = publisher
        self.name = name
        self.authors = authros
        self.teaching_work_type = teaching_work_type

    teaching_work_id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(50))
    name = db.Column(db.String(50))
    authors = db.Column(db.String(150))
    teaching_work_type = db.Column(db.String(50))

    teachers = db.relationship(
        "Teacher",
        secondary=TeachingWork_teacher,
        backref="teaching_works",
    )

    def __repr__(self):
        return f"id: {self.teaching_work_id}, publisher: {self.publisher}, name: {self.name}, authors: {self.authors}, type: {self.teaching_work_type}"
    
    def compare(self, other):
        if self.publisher != other.publisher:
            return False
        if self.name != other.name:
            return False
        if self.authors != other.authors:
            return False
        if self.teaching_work_type != other.teaching_work_type:
            return False

        return True


class Speech(db.Model):
    __tablename__ = "speeches"

    def __init__(self, name, location, date, teacher_id):
        self.name = name
        self.location = location
        self.date = date
        self.teacher_id = teacher_id

    speech_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date = db.Column(db.Date)
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="speeches")

    def __repr__(self):
        return f"id: {self.speech_id}, name: {self.speech_id}, location: {self.location}, date: {self.date}, teacher_id: {self.teacher_id}"


# awards_and_honors
class Award(db.Model):
    __tablename__ = "awards"

    def __init__(self, government, award_name, year, students, teacher_id):
        self.government = government
        self.award_name = award_name
        self.year = year
        self.students = students
        self.teacher_id = teacher_id

    award_id = db.Column(db.Integer, primary_key=True)
    government = db.Column(db.String(50))
    award_name = db.Column(db.String(50))
    year = db.Column(db.Integer)
    students = db.Column(db.String(50))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="awards")

    def __repr__(self):
        return f"id: {self.award_id}, government: {self.government}, award name: {self.award_name}, year: {self.year}, students: {self.students}, teacher id: {self.teacher_id}"


class ProceedingArtical(db.Model):
    __tablename__ = "proceeding_articals"

    def __init__(
        self,
        artical_name,
        collaborators,
        page_number_of_the_artical,
        session_venue,
        time,
    ):
        self.artical_name = artical_name
        self.collaborators = collaborators
        self.page_number_of_the_artical = page_number_of_the_artical
        self.session_venue = session_venue
        self.time = time

    proceeding_artical_id = db.Column(db.Integer, primary_key=True)
    artical_name = db.Column(db.String(150))
    collaborators = db.Column(db.String(150))
    page_number_of_the_artical = db.Column(db.String(50))
    session_venue = db.Column(db.String(50))
    time = db.Column(db.Date)

    teachers = db.relationship(
        "Teacher", secondary=ProceedingArtical_teacher, backref="proceeding_articals"
    )

    def __repr__(self):
        return f"id: {self.proceeding_artical_id}, artical name: {self.artical_name}, collaborators: {self.collaborators}, page number of the artical: {self.page_number_of_the_artical}, session venue: {self.session_venue}, time: {self.time}"

    def compare(self, other):
        if self.artical_name != other.artical_name:
            return False
        if self.collaborators != other.collaborators:
            return False
        if self.page_number_of_the_artical != other.page_number_of_the_artical:
            return False
        if self.session_venue != other.session_venue:
            return False
        if self.time != other.time:
            return False
        return True

    def to_dict(self):
        return {field.name:getattr(self, field.name) for field in self.__table__.c}

class BookChapter(db.Model):
    __tablename__ = "book_chapters"

    def __init__(self, book_name, collaborators, page_number_of_the_artical, time):
        self.book_name = book_name
        self.collaborators = collaborators
        self.page_number_of_the_artical = page_number_of_the_artical
        self.time = time

    book_chapter_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50))
    collaborators = db.Column(db.String(150))
    page_number_of_the_artical = db.Column(db.String(50))
    time = db.Column(db.Date)

    teachers = db.relationship(
        "Teacher", secondary=BookChapter_teacher, backref="book_chapters"
    )

    def __repr__(self):
        return f"id: {self.book_chapter_id}, book name: {self.book_name}, collaborators: {self.collaborators}, page number of the artical: {self.page_number_of_the_artical}, time: {self.time}"

    def compare(self, other):
        if self.book_name != other.book_name:
            return False
        if self.collaborators != other.collaborators:
            return False
        if self.page_number_of_the_artical != other.page_number_of_the_artical:
            return False
        if self.time != other.time:
            return False

        return True


# books_and_technical_reports
class BookReport(db.Model):
    __tablename__ = "book_reports"

    def __init__(self, book_report_type, authors, name, publisher, country, date):
        self.book_report_type = book_report_type
        self.authors = authors
        self.name = name
        self.publisher = publisher
        self.country = country
        self.date = date

    book_report_id = db.Column(db.Integer, primary_key=True)
    book_report_type = db.Column(db.String(50))
    authors = db.Column(db.String(150))
    name = db.Column(db.String(50))
    publisher = db.Column(db.String(50))
    country = db.Column(db.String(50))
    date = db.Column(db.Date)

    teachers = db.relationship(
        "Teacher",
        secondary=BookReport_teacher,
        backref="book_reports",
    )

    def __repr__(self):
        return f"id: {self.book_report_id}, book and technical report type: {self.book_report_type}, authors: {self.authors}, name: {self.name}, publisher: {self.publisher}, country: {self.country}, date: {self.date}"
    
    def compare(self, other):
        if self.book_report_type != other.book_report_type:
            return False
        if self.authors != other.authors:
            return False
        if self.name != other.name:
            return False
        if self.publisher != other.publisher:
            return False
        if self.country != other.country:
            return False
        if self.date != other.date:
            return False
        return True

    def to_dict(self):
        return {field.name:getattr(self, field.name) for field in self.__table__.c}


# national_science_and_technology_council_projects
class NationalProject(db.Model):
    __tablename__ = "national_projects"

    def __init__(self, name, time, number, attribute, host, teacher_id):
        self.name = name
        self.time = time
        self.number = number
        self.attribute = attribute
        self.host = host
        self.teacher_id = teacher_id

    national_project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    time = db.Column(db.Date)
    number = db.Column(db.String(50))
    attribute = db.Column(db.String(50))
    host = db.Column(db.String(20))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="national_projects")

    def __repr__(self):
        return f"id: {self.national_project_id}, name: {self.name}, time: {self.time}, number: {self.number}, attribute: {self.attribute}, host: {self.host}, teacher_id: {self.teacher_id}"


# university_industry_cooperation_projects
class UniversityProject(db.Model):
    __tablename__ = "university_projects"

    def __init__(self, name, time, host, teacher_id):
        self.name = name
        self.time = time
        self.host = host
        self.teacher_id = teacher_id

    university_project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    time = db.Column(db.Date)
    host = db.Column(db.String(20))
    teacher_id = db.Column(db.ForeignKey("teachers.teacher_id"))

    teacher = db.relationship("Teacher", backref="university_projects")

    def __repr__(self):
        return f"id: {self.university_project_id}, name: {self.name}, time: {self.time}, host: {self.host}, teacher_id: {self.teacher_id}"

