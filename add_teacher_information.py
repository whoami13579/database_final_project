import sqlite3

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

journalArticals = [
    (1, "Blockchain-based pipeline custody system (BPCS) for preserving critical video evidence", "Journal of Internet Technology", "Fan, Y.Y., Chew, C. J., Hong, W. Z., Chen, Y. C., Lee, J.S.*", "447-454", "SCIE" ,"2024-06-03"),
    (2, "Preserving Manipulated and Synthetic Deepfake Detection through Face Texture Naturalness", "Accepted byJournal of Information Security and Applications", "Chew, C. J., Lin, Y. C., Chen, Y. C., Fan, Y.Y., and Lee, J.S.*", "000", "SCIE" ,"2024-05-01"),
]
cur.executemany("INSERT INTO journal_articals VALUES(?, ?, ?, ?, ?, ?, ?)", journalArticals)

JournalArtical_teacher = [
    (1, 1),
    (1, 2),
]
cur.executemany("INSERT INTO journalArtical_teachers VALUES(?, ?)", JournalArtical_teacher)


proceeding_articals = [
    (1, "Enhancing Data Embedding Capacity in Encrypted Images via Adaptive MSB Prediction", "Chang, C.W., Lee, J.S., and Chou, Y.C.", "1-9, 2024-03", "2024 6th International Conference on Image, Video and Signal Processing (IVSP 2024)", "2024-03-01"),
    (2, "Preserving Collusion-free and Traceability in Car-sharing System based on Blockchain", "Chen, T.H., Chew, C. J., Chen, Y. C., and Lee, J.S", "1-12", "International Computer Symposium (ICS 2022),", "2022-12-01"),
]
cur.executemany("INSERT INTO proceeding_articals VALUES(?, ?, ?, ?, ?, ?)", proceeding_articals)

proceedingArtical_teacher = [
    (1, 1),
    (1, 2),
]
cur.executemany("INSERT INTO proceedingArtical_teacher VALUES(?, ?)", proceedingArtical_teacher)


book_reports = [
    (1, "專業書籍", "王旭正、李榮三、魏國瑞", "資訊生活安全、行動智慧應用與網駭實務", "博碩 出版", "中華民國", "2020-09-01"),
    (2, "專業書籍", "王旭正、李榮三、許富皓", "資訊安全與智慧、行動網路安全應用實務", "博碩 出版", "中華民國", "2015-08-01"),
]
cur.executemany("INSERT INTO book_reports VALUES(?, ?, ?, ?, ?, ?, ?)", book_reports)

bookReport_teacher = [
    (1, 1),
    (1, 2),
]
cur.executemany("INSERT INTO bookReport_teacher VALUES(?, ?)", bookReport_teacher)


national_projects = [
    (1, "(博士增核)基於行為分析與後量子密碼區塊鏈之動態零信任驗證框架(1/3)", "2023-10-01", "", "NSTC112-2221-E-035-050-MY3", "主持人", 1),
    (2, "基於行為分析與後量子密碼區塊鏈之動態零信任驗證框架(1/3)", "2023-08-01", "", "NSTC112-2221-E-035-050-MY3", "主持人", 1),
]
cur.executemany("INSERT INTO national_projects VALUES(?, ?, ?, ?, ?, ?, ?)", national_projects)


con.commit()
