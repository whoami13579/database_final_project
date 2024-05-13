import sqlite3

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

roles = [
    (1, "系主任"),
    (2, "榮譽特聘講座"),
    (3, "講座教授"),
    (4, "特約講座"),
    (5, "特聘教授"),
    (6, "專任教師"),
    (7, "兼任教師"),
    (8, "行政人員"),
    (9, "退休教師"),
]
cur.executemany("INSERT INTO roles VALUES(?, ?)", roles)
con.commit()
