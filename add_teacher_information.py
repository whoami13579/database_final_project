import sqlite3

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

journalArticals = [
    (1, "Blockchain-based pipeline custody system (BPCS) for preserving critical video evidence", "Journal of Internet Technology", "Fan, Y.Y., Chew, C. J., Hong, W. Z., Chen, Y. C., Lee, J.S.*", "447-454", "SCIE" ,"2024-06-03"),
    (2, "Preserving Manipulated and Synthetic Deepfake Detection through Face Texture Naturalness", "Accepted byJournal of Information Security and Applications", "Chew, C. J., Lin, Y. C., Chen, Y. C., Fan, Y.Y., and Lee, J.S.*", "000", "SCIE" ,"2024-05-01"),
]
cur.executemany("INSERT INTO journal_articals VALUES(?, ?, ?, ?, ?, ?, ?)", journalArticals)
    # journal_artical_id = db.Column(db.Integer, primary_key=True)
    # course_name = db.Column(db.String(50))
    # journal_name = db.Column(db.String(50))
    # collaborators = db.Column(db.String(50))
    # page_number_of_the_journal = db.Column(db.String(50))
    # indexed_website = db.Column(db.String(150))
    # indexed_time = db.Column(db.Date)


JournalArtical_teacher = [
    (1, 1),
    (1, 2),
]
cur.executemany("INSERT INTO journalArtical_teachers VALUES(?, ?)", JournalArtical_teacher)
con.commit()

