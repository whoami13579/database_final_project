from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Role, Teacher, ClassSchedule, JournalArtical, ProceedingArtical, BookReport, NationalProject, UniversityProject, Award, Reward, Speech, BookChapter, TeachingWork, InternalExperience, ExternalExperience
from . import db
from datetime import datetime
import os, sys

views = Blueprint("views", __name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "static/images/")

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

@views.route("/teacher/<int:teacher_id>/class-schedule")
def class_schedule(teacher_id):
    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()

    classes = ClassSchedule.query.filter_by(teacher_id=teacher_id).all()
    print("classes: ", classes, file=sys.stdout)

    schedules_table = [[list() for _ in range(14)] for _ in range(8)]
    print("schedules_table before: ", schedules_table)
    for c in classes:
        print(c, type(c))
        schedules_table[c.week-1][c.time-1] = [c.schedule_id, c.name]
    print("schedules_table after: ", schedules_table)

    # schedules = teacher.class_schedules
    # print(schedules[0], schedules[0].schedule_id, type(schedules[0]), file=sys.stdout)
    # schedules_table = []
    # for i in range(8):
    #     schedules_table.append([" "]*14)
    
    # for schedule in schedules:
    #     schedules_table[schedule.week-1][schedule.time-1] = (schedule.name)
    # print(schedules_table[0], type(schedules_table), file=sys.stdout)

    return render_template("class_schedule.html", user=current_user, teacher=teacher, schedules_table=schedules_table)

@views.route("/teacher/<int:teacher_id>/class-schedule/add-class-schedule", methods=['GET', 'POST'])
@login_required
def add_class_schedule(teacher_id):
    if request.method == "POST":
        week = request.form.get("week")
        time = request.form.get("time")
        name = request.form.get("name")
        # teacher_id = current_user.get_id()

        if ClassSchedule.query.filter_by(week=week, time=time, teacher_id=teacher_id).first():
            class_schedule = ClassSchedule.query.filter_by(week=week, time=time, teacher_id=teacher_id).first()
            # if class_schedule.compare(class_schedule):
            #     class_schedule.teachers.append(current_user)
            #     db.session.commit()
            # if class_schedule is not None:
            #     classSchedule = ClassSchedule(week, time, name, teacher_id)
            #     db.session.add(classSchedule)
            #     db.session.commit()
            #     flash("Add Class", category="success")

            #     # return redirect(url_for("views.class_schedule", teacher_id=teacher_id))
            # else:
            flash("This Class already exists", category="error")
            return render_template("add_class.html", user=current_user, teacher=Teacher.query.filter_by(teacher_id=current_user.get_id()).first())

        else:
            classSchedule = ClassSchedule(week, time, name, teacher_id)
            classSchedule.teacher = current_user
            db.session.add(classSchedule)
            db.session.commit()

            flash("Add Class", category="success")
            # return redirect(url_for("views.class_schedule", teacher_id=teacher_id))

        teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
        classes = ClassSchedule.query.filter_by(teacher_id=teacher_id).all()
        schedules_table = [[list() for _ in range(14)] for _ in range(8)]
        for c in classes:
            # print(c, type(c))
            schedules_table[c.week-1][c.time-1] = [c.schedule_id, c.name]
        return render_template("class_schedule.html", user=current_user, teacher=teacher, schedules_table=schedules_table)
    else:
        return render_template("add_class.html", user=current_user, teacher=Teacher.query.filter_by(teacher_id=current_user.get_id()).first())


@views.route("/teacher/<int:teacher_id>/class-schedule/update-class-schedule/<int:schedule_id>", methods=['GET', 'POST'])
@login_required
def update_class_schedule(teacher_id, schedule_id):
    class_schedule = ClassSchedule.query.get(schedule_id)
    if request.method == "POST":
        class_schedule.week = request.form.get("week")
        class_schedule.time = request.form.get("time")
        class_schedule.name = request.form.get("name")
        db.session.commit()

        flash("Update Class", category="success")

        teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
        classes = ClassSchedule.query.filter_by(teacher_id=teacher_id).all()
        schedules_table = [[list() for _ in range(14)] for _ in range(8)]
        for c in classes:
            # print(c, type(c))
            schedules_table[c.week-1][c.time-1] = [c.schedule_id, c.name]
        return render_template("class_schedule.html", user=current_user, teacher=teacher, schedules_table=schedules_table)
        # return redirect(url_for("views.class_schedule", teacher_id=teacher_id))
        # return render_template("class_schedule.html", user=current_user, teacher=Teacher.query.filter_by(teacher_id=teacher_id).first())
        
    else:
        teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
        return render_template("update_class_schedule.html", user=current_user, teacher=teacher, class_schedule=class_schedule)

@views.route("/teacher/<int:teacher_id>/class-schedule/delete-class-schedule/<int:schedule_id>", methods=['POST', 'GET'])
@login_required
def delete_class_schedule(teacher_id, schedule_id):
    the_class = ClassSchedule.query.filter_by(schedule_id=schedule_id).first()
    db.session.delete(the_class)
    db.session.commit()

    flash("Delete Class", category='success')

    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    classes = ClassSchedule.query.filter_by(teacher_id=teacher_id).all()
    schedules_table = [[list() for _ in range(14)] for _ in range(8)]
    for c in classes:
        print(c, type(c))
        schedules_table[c.week-1][c.time-1] = [c.schedule_id, c.name]
    return render_template("class_schedule.html", user=current_user, teacher=teacher, schedules_table=schedules_table)
    # return redirect(url_for("views.class_schedule", teacher_id=teacher_id))

    

@views.route("/add-journal-artical/", methods=["GET", "POST"])
@login_required
def add_journal_artical():
    if request.method == "POST":
        course_name = request.form.get("course_name")
        journal_name = request.form.get("journal_name")
        collaborators = request.form.get("collaborators")
        page_number_of_the_journal = request.form.get("page_number_of_the_journal")
        # page_number_of_the_journal = int(page_number_of_the_journal)
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

        # if host == "0":
        #     flash("請選擇職位名稱", category="error")
        #     return render_template("add_national_project.html", user=current_user)

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

        # if host == "0":
        #     flash("請選擇職位名稱", category="error")
        #     return render_template("add_university_project.html", user=current_user)

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


# Modification Part
@views.route("/teacher/<teacher_id>/modify-journal-artical/<journal_artical_id>", methods=["GET", "POST"])
@login_required
def modify_journal_artical(teacher_id, journal_artical_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(JournalArtical).filter_by(journal_artical_id=journal_artical_id).first()
        artical_to_mod = artical.to_dict()
        return render_template("modify_journal_artical.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        indexed_time = submission["indexed_time"]
        date_format = "%Y-%m-%d"
        submission["indexed_time"] = datetime.strptime(indexed_time, date_format).date()

        artical = db.session.query(JournalArtical).filter_by(journal_artical_id=journal_artical_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Journal Artical", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-proceeding-artical/<proceeding_artical_id>", methods=["GET", "POST"])
@login_required
def modify_proceeding_artical(teacher_id, proceeding_artical_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(ProceedingArtical).filter_by(proceeding_artical_id=proceeding_artical_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_proceeding_artical.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        time = submission["time"]
        date_format = "%Y-%m-%d"
        submission["time"] = datetime.strptime(time, date_format).date()

        artical = db.session.query(ProceedingArtical).filter_by(proceeding_artical_id=proceeding_artical_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Proceeding Artical", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-book-report/<book_report_id>", methods=["GET", "POST"])
@login_required
def modify_book_report(teacher_id, book_report_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(BookReport).filter_by(book_report_id=book_report_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_book_report.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        date = submission["date"]
        date_format = "%Y-%m-%d"
        submission["date"] = datetime.strptime(date, date_format).date()
        artical = db.session.query(BookReport).filter_by(book_report_id=book_report_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Book Report", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-national-project/<national_project_id>", methods=["GET", "POST"])
@login_required
def modify_national_project(teacher_id, national_project_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(NationalProject).filter_by(national_project_id=national_project_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_national_project.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        time = submission["time"]
        date_format = "%Y-%m-%d"
        submission["time"] = datetime.strptime(time, date_format).date()
        artical = db.session.query(NationalProject).filter_by(national_project_id=national_project_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify National Project", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-university-project/<university_project_id>", methods=["GET", "POST"])
@login_required
def modify_university_project(teacher_id, university_project_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(UniversityProject).filter_by(university_project_id=university_project_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_university_project.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        time = submission["time"]
        date_format = "%Y-%m-%d"
        submission["time"] = datetime.strptime(time, date_format).date()
        artical = db.session.query(UniversityProject).filter_by(university_project_id=university_project_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify University Project", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-award/<award_id>", methods=["GET", "POST"])
@login_required
def modify_award(teacher_id, award_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(Award).filter_by(award_id=award_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_award.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        submission["year"] = int(submission["year"])
        artical = db.session.query(Award).filter_by(award_id=award_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Award", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-reward/<reward_id>", methods=["GET", "POST"])
@login_required
def modify_reward(teacher_id, reward_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(Reward).filter_by(reward_id=reward_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_reward.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        reward_time = submission["reward_time"]
        date_format = "%Y-%m-%d"
        submission["reward_time"] = datetime.strptime(reward_time, date_format).date()
        artical = db.session.query(Reward).filter_by(reward_id=reward_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Reward", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-speech/<speech_id>", methods=["GET", "POST"])
@login_required
def modify_speech(teacher_id, speech_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(Speech).filter_by(speech_id=speech_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_speech.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        date = submission["date"]
        date_format = "%Y-%m-%d"
        submission["date"] = datetime.strptime(date, date_format).date()
        artical = db.session.query(Speech).filter_by(speech_id=speech_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Speech", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-book-chapter/<book_chapter_id>", methods=["GET", "POST"])
@login_required
def modify_book_chapter(teacher_id, book_chapter_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(BookChapter).filter_by(book_chapter_id=book_chapter_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_book_chapter.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        time = submission["time"]
        date_format = "%Y-%m-%d"
        submission["time"] = datetime.strptime(time, date_format).date()
        artical = db.session.query(BookChapter).filter_by(book_chapter_id=book_chapter_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Book Chapter", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/modify-teaching-work/<teaching_work_id>", methods=["GET", "POST"])
@login_required
def modify_teaching_work(teacher_id, teaching_work_id):
    # If user wants to modify
    if request.method == "GET":
        artical = db.session.query(TeachingWork).filter_by(teaching_work_id=teaching_work_id).first()
        artical_to_mod = artical.to_dict()

        return render_template("modify_teaching_work.html", user=current_user.get_id(), artical_to_mod=artical_to_mod)
    # Else if user submit the modify
    else:
        submission = request.form.to_dict()
        artical = db.session.query(TeachingWork).filter_by(teaching_work_id=teaching_work_id)
        artical.update(submission)

        db.session.commit()
        flash("Modify Teaching Work", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))


# Deletion Part
@views.route("/teacher/<teacher_id>/delete-journal-artical/<journal_artical_id>", methods=["POST"])
@login_required
def delete_journal_artical(teacher_id, journal_artical_id):
    artical = db.session.query(JournalArtical).filter_by(journal_artical_id=journal_artical_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Journal Artical", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-proceeding-artical/<proceeding_artical_id>", methods=["POST"])
@login_required
def delete_proceeding_artical(teacher_id, proceeding_artical_id):
    artical = db.session.query(ProceedingArtical).filter_by(proceeding_artical_id=proceeding_artical_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Proceeding Artical", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-book-report/<book_report_id>", methods=["GET", "POST"])
@login_required
def delete_book_report(teacher_id, book_report_id):
    artical = db.session.query(BookReport).filter_by(book_report_id=book_report_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Book Report", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-national-project/<national_project_id>", methods=["GET", "POST"])
@login_required
def delete_national_project(teacher_id, national_project_id):
    artical = db.session.query(NationalProject).filter_by(national_project_id=national_project_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete National Project", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-university-project/<university_project_id>", methods=["GET", "POST"])
@login_required
def delete_university_project(teacher_id, university_project_id):
    artical = db.session.query(UniversityProject).filter_by(university_project_id=university_project_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete University Project", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-award/<award_id>", methods=["GET", "POST"])
@login_required
def delete_award(teacher_id, award_id):
    artical = db.session.query(Award).filter_by(award_id=award_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Award", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-reward/<reward_id>", methods=["GET", "POST"])
@login_required
def delete_reward(teacher_id, reward_id):
    artical = db.session.query(Reward).filter_by(reward_id=reward_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Reward", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-speech/<speech_id>", methods=["GET", "POST"])
@login_required
def delete_speech(teacher_id, speech_id):
    artical = db.session.query(Speech).filter_by(speech_id=speech_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Speech", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-book-chapter/<book_chapter_id>", methods=["GET", "POST"])
@login_required
def delete_book_chapter(teacher_id, book_chapter_id):
    artical = db.session.query(BookChapter).filter_by(book_chapter_id=book_chapter_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Book Chapter", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/delete-teaching-work/<teaching_work_id>", methods=["GET", "POST"])
@login_required
def delete_teaching_work(teacher_id, teaching_work_id):
    artical = db.session.query(TeachingWork).filter_by(teaching_work_id=teaching_work_id).first()
    db.session.delete(artical)
    db.session.commit()
    flash("Delete Teaching Work", category="success")
    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))


# Edit introduction
@views.route("/teacher/<teacher_id>/edit-introduction", methods=["GET", "POST"])
@login_required
def edit_introduction(teacher_id):
    teacher = Teacher.query.filter_by(teacher_id = teacher_id).first()
    if request.method == "POST":
        self_introduction = request.form.get("introduction")
        teacher.self_introduction = self_introduction

        db.session.commit()
        flash("Change saved", category="success")

        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

    return render_template("self_introduction.html", user=current_user, teacher=teacher)


@views.route("/teacher/<teacher_id>/edit-school", methods=["GET", "POST"])
@login_required
def edit_school(teacher_id):
    teacher = Teacher.query.filter_by(teacher_id = teacher_id).first()
    if request.method == "POST":
        school = request.form.get("school")
        teacher.school = school

        db.session.commit()
        flash("Change saved", category="success")

        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

    return render_template("school.html", user=current_user, teacher=teacher)


@views.route("/teacher/<teacher_id>/edit-photo", methods=["POST"])
@login_required
def edit_photo(teacher_id):
    img = request.files['img']
    if img.filename != '':
        # Save image file
        file_name = teacher_id + os.path.splitext(os.path.basename(img.filename))[1]
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        img.save(file_path)
        # Update database
        teacher = Teacher.query.filter_by(teacher_id = teacher_id).first()
        teacher.photo = file_name
        db.session.commit()
    else:
        flash("Please choose an image", category='error')

    return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

@views.route("/teacher/<teacher_id>/edit-interest", methods=["GET", "POST"])
@login_required
def edit_interest(teacher_id):
    teacher = Teacher.query.filter_by(teacher_id = teacher_id).first()
    if request.method == "POST":
        interest = request.form.get("interest")
        teacher.interest = interest

        db.session.commit()
        flash("Change saved", category="success")

        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

    return render_template("interest.html", user=current_user, teacher=teacher)


@views.route("/add-internal-experience/", methods=["GET", "POST"])
@login_required
def add_internal_experience():
    if request.method == "POST":
        department = request.form.get("department")
        position = request.form.get("position")

        experience = InternalExperience(department, position, current_user.get_id())

        experience.teacher = current_user
        db.session.add(experience)
        db.session.commit()

        flash("Add Internal Experience", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

    return render_template("add_internal_experience.html", user=current_user)


@views.route("/add-external-experience/", methods=["GET", "POST"])
@login_required
def add_external_experience():
    if request.method == "POST":
        date = request.form.get("date")
        school = request.form.get("school")
        department = request.form.get("department")
        position = request.form.get("position")

        date_format = "%Y-%m-%d"
        date = datetime.strptime(date, date_format).date()

        experience = ExternalExperience(date, school, department, position, current_user.get_id())

        experience.teacher = current_user
        db.session.add(experience)
        db.session.commit()

        flash("Add Internal Experience", category="success")
        return redirect(url_for("views.teacher", teacher_id=current_user.get_id()))

    return render_template("add_external_experience.html", user=current_user)
