from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Role, Teacher, ClassSchedule, JournalArtical, ProceedingArtical, BookReport, NationalProject, UniversityProject, Award, Reward, Speech, BookChapter, TeachingWork
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

@views.route("/teacher/<teacher_id>/class-schedule")
def class_schedule(teacher_id):
    return render_template("class_schedule.html", user=current_user, teacher=Teacher.query.filter_by(teacher_id=teacher_id).first())

@views.route("/teacher/<teacher_id>/class-schedule/add-class", methods=['GET', 'POST'])
def add_class_schedule(teacher_id):
    if request.method == "POST":
        week = request.form.get("week")
        time = request.form.get("time")
        name = request.form.get("name")
        teacher_id = request.form.get("teacher_id")

        classSchedule = ClassSchedule(week, time, name, teacher_id)
        db.session.add(classSchedule)
        db.session.commit()

        #return redirect(url_for("views.class_schedule", teacher_id=current_user.get_id()))
        
    #else:
    return render_template("add_class.html", user=current_user, teacher=Teacher.query.filter_by(teacher_id=teacher_id).first())

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
                flash("Proceeding Artical already exists", category="error")
        else:
            # current_user.proceeding_articals.append(proceedingArtical)
            proceedingArtical.teachers.append(current_user)
            db.session.add(proceedingArtical)
            db.session.commit()

            flash("Add Proceeding Artical", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_proceeding_artical.html", user=current_user)


@views.route("/add-book-report/", methods=["GET", "POST"])
@login_required
def add_book_report():
    if request.method == "POST":
        book_report_type = request.form.get("book_report_type")
        authors = request.form.get("authors")
        name = request.form.get("name")
        publisher = request.form.get("publisher")
        country = request.form.get("country")
        date = request.form.get("date")
        date_format = "%Y-%m-%d"
        date = datetime.strptime(date, date_format).date()
        bookReport = BookReport(book_report_type, authors, name, publisher, country, date)

        book = BookReport.query.filter_by(name=name).first()
        
        if book:
            if book.compare(bookReport):
                book.teachers.append(current_user)
                # current_user.book_reports.append(bookReport)
                db.session.commit()

                return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
            else:
                flash("Book Report already exists", category="error")
        else:
            # current_user.book_reports.append(bookReport)
            bookReport.teachers.append(current_user)
            db.session.add(bookReport)
            db.session.commit()

            flash("Add Book Report", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_book_report.html", user=current_user)


@views.route("/add-national-project/", methods=["GET", "POST"])
@login_required
def add_national_project():
    if request.method == "POST":
        name = request.form.get("name")
        time = request.form.get("time")
        number = request.form.get("number")
        attribute = request.form.get("attribute")
        host = request.form.get("host")

        if host == "0":
            flash("請選擇職位名稱", category="error")
            return render_template("add_national_project.html", user=current_user)

        date_format = "%Y-%m-%d"
        time = datetime.strptime(time, date_format).date()
        nationalProject = NationalProject(name, time, number, attribute, host, current_user.get_id())

        project = NationalProject.query.filter_by(name=name).first()
        
        if project:
            flash("National Project already exists", category="error")
            return render_template("add_national_project.html", user=current_user)
        else:
            # current_user.national_projects.append(nationalProject)
            nationalProject.teacher = current_user
            db.session.add(nationalProject)
            db.session.commit()

            flash("Add National Project", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_national_project.html", user=current_user)


@views.route("/add-university-project/", methods=["GET", "POST"])
@login_required
def add_university_project():
    if request.method == "POST":
        name = request.form.get("name")
        time = request.form.get("time")
        host = request.form.get("host")

        if host == "0":
            flash("請選擇職位名稱", category="error")
            return render_template("add_university_project.html", user=current_user)
        

        date_format = "%Y-%m-%d"
        time = datetime.strptime(time, date_format).date()
        universityProject = UniversityProject(name, time, host, current_user.get_id())

        project = UniversityProject.query.filter_by(name=name).first()
        
        if project:
            flash("University Project already exists", category="error")
            return render_template("add_university_project.html", user=current_user)
        else:
            # current_user.university_projects.append(universityProject)
            universityProject.teacher = current_user
            db.session.add(universityProject)
            db.session.commit()

            flash("Add University Project", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_university_project.html", user=current_user)


@views.route("/add-award/", methods=["GET", "POST"])
@login_required
def add_award():
    if request.method == "POST":
        government = request.form.get("government")
        award_name = request.form.get("award_name")
        year = int(request.form.get("year"))
        students = request.form.get("students")
        
        
        if Award.query.filter_by(award_name=award_name).first():
            flash("The award already exists", category="error")
            return render_template("add_award.html", user=current_user)
        else:
            award = Award(government, award_name, year, students, current_user.get_id())
            # current_user.awards.append(award)
            award.teacheri = current_user
            db.session.add(award)
            db.session.commit()

            flash("Add Awards", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_award.html", user=current_user)

@views.route("/add-reward/", methods=["GET", "POST"])
@login_required
def add_reward():
    if request.method == "POST":
        reward_time = request.form.get("reward_time")
        award = request.form.get("award")
        school = request.form.get("school")
        attribute = request.form.get("attribute")
        name = request.form.get("name")
        date_format = "%Y-%m-%d"
        reward_time = datetime.strptime(reward_time, date_format).date()
        reward = Reward(reward_time, award, school, attribute, name, current_user.get_id())
        
        if Reward.query.filter_by(name=name).first():
            flash("The reward already exists", category="error")
            return render_template("add_reward.html", user=current_user)
        else:
            # current_user.awards.append(reward)
            Reward.teacher = current_user
            db.session.add(reward)
            db.session.commit()

            flash("Add Rewards", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_reward.html", user=current_user)


@views.route("/add-speech/", methods=["GET", "POST"])
@login_required
def add_speech():
    if request.method == "POST":
        name = request.form.get("name")
        location = request.form.get("location")
        date = request.form.get("date")
        date_format = "%Y-%m-%d"
        date = datetime.strptime(date, date_format).date()
        speech = Speech(name, location, date, current_user.get_id())
        
        if Speech.query.filter_by(name=name).first():
            flash("The Speech already exists", category="error")
            return render_template("add_speech.html", user=current_user)
        else:
            # current_user.speeches.append(speech)
            speech.teacher = current_user
            db.session.add(speech)
            db.session.commit()

            flash("Add Speeches", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_speech.html", user=current_user)

# --------------------
@views.route("/add-teaching-work/", methods=["GET", "POST"])
@login_required
def add_teaching_work():
    if request.method == "POST":
        publisher = request.form.get("publisher")
        name = request.form.get("name")
        authors = request.form.get("authors")
        teaching_work_type = request.form.get("teaching_work_type")
        teachingWork = TeachingWork(publisher, name, authors, teaching_work_type)
        
        if TeachingWork.query.filter_by(name=name).first():
            work = TeachingWork.query.filter_by(name=name).first()
            if work.compare(teachingWork):
                work.teachers.append(current_user)
                # current_user.teaching_works.append(teachingWork)
                db.session.commit()

                return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
            else:
                flash("The TeachingWork already exists", category="error")
        else:
            # current_user.teaching_works.append(teachingWork)
            teachingWork.teachers.append(current_user)
            db.session.add(teachingWork)
            db.session.commit()

            flash("Add TeachingWorkes", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_teaching_work.html", user=current_user)

@views.route("/add-book-chapter/", methods=["GET", "POST"])
@login_required
def add_book_chapter():
    if request.method == "POST":
        book_name = request.form.get("book_name")
        collaborators = request.form.get("collaborators")
        page_number_of_the_artical = request.form.get("page_number_of_the_artical")
        time = request.form.get("time")
        date_format = "%Y-%m-%d"
        time = datetime.strptime(time, date_format).date()
        bookChapter = BookChapter(book_name, collaborators, page_number_of_the_artical, time)
        
        if BookChapter.query.filter_by(book_name=book_name).first():
            book = BookChapter.query.filter_by(book_name=book_name).first()
            if book.compare(bookChapter):
                book.teachers.append(current_user)
                # current_user.book_chapters.append(bookChapter)
                db.session.commit()

                return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
            else:
                flash("The Patent already exists", category="error")
        else:
            # current_user.book_chapters.append(bookChapter)
            bookChapter.teachers.append(current_user)
            db.session.add(bookChapter)
            db.session.commit()

            flash("Add Patentes", category="success")
            return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))
    return render_template("add_book_chapter.html", user=current_user)
