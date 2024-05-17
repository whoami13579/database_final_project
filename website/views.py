from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Role, Teacher, JournalArtical, ProceedingArtical
from . import db
from datetime import datetime

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", user=current_user, teachers=Teacher.query.all(), roles=Role.query.all())


@views.route("/role/<role_id>")
def role(role_id):
    return render_template("role.html", user=current_user, role=Role.query.filter_by(role_id=role_id).first())


@views.route("/teacher/<teacher_id>")
def teacher(teacher_id):
    return render_template("teacher.html", user=current_user, teacher=Teacher.query.filter_by(teacher_id=teacher_id).first())


@views.route("/add-journal-artical/", methods=["GET", "POST"])
@login_required
def add_journal_artical():
    if request.method == "POST":
        course_name = request.form.get("course_name")
        journal_name = request.form.get("journal_name")
        collaborators = request.form.get("collaborators")
        page_number_of_the_journal = request.form.get("page_number_of_the_journal")
        page_number_of_the_journal = int(page_number_of_the_journal)
        indexed_website = request.form.get("indexed_website")
        indexed_time = request.form.get("indexed_time")
        date_format = "%Y-%m-%d"
        indexed_time = datetime.strptime(indexed_time, date_format).date()
        journalArtical = JournalArtical(course_name, journal_name, collaborators, page_number_of_the_journal, indexed_website, indexed_time)
        
        if JournalArtical.query.filter_by(course_name=course_name).first():
            artical = JournalArtical.query.filter_by(course_name=course_name).first()
            if artical.compare(journalArtical):
                artical.teachers.append(current_user)
                # current_user.journal_articals.append(journalArtical)
                db.session.commit()

                return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
            else:
                flash("Journal Artical already exists", category="error")
        else:
            # current_user.journal_articals.append(journalArtical)
            journalArtical.teachers.append(current_user)
            db.session.add(journalArtical)
            db.session.commit()

            flash("Add Journal Artical", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_journal_artical.html", user=current_user)


@views.route("/add-proceeding-artical/", methods=["GET", "POST"])
@login_required
def add_proceeding_artical():
    if request.method == "POST":
        artical_name = request.form.get("artical_name")
        collaborators = request.form.get("collaborators")
        page_number_of_the_artical = request.form.get("page_number_of_the_artical")
        session_venue = request.form.get("session_venue")
        time = request.form.get("time")
        date_format = "%Y-%m-%d"
        time = datetime.strptime(time, date_format).date()
        proceedingArtical = ProceedingArtical(artical_name, collaborators, page_number_of_the_artical, session_venue, time)
        
        if ProceedingArtical.query.filter_by(artical_name=artical_name).first():
            artical = ProceedingArtical.query.filter_by(artical_name=artical_name).first()
            if artical.compare(proceedingArtical):
                artical.teachers.append(current_user)
                # current_user.proceeding_articals.append(proceedingArtical)
                db.session.commit()

                return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
            else:
                flash("Journal Artical already exists", category="error")
        else:
            # current_user.proceeding_articals.append(proceedingArtical)
            proceedingArtical.teachers.append(current_user)
            db.session.add(proceedingArtical)
            db.session.commit()

            flash("Add Journal Artical", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_proceeding_artical.html", user=current_user)
