import sqlite3
from werkzeug.security import generate_password_hash

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

teachers = [
    (1, "leejs@fcu.edu.tw", "李榮三", generate_password_hash("111111"), None, None, None, None, None, 1),
    (2, "tcyang@fcu.edu.tw", "楊濬中", generate_password_hash("222222"), None, None, None, None, None, 2),
    (3, "acliu@fcu.edu.tw", "劉安之", generate_password_hash("222222"), None, None, None, None, None, 2),
    (4, "alan3c@gmail.com", "張真誠", generate_password_hash("333333"), None, None, None, None, None, 3),
    (5, "wheyming_song@yahoo.com", "桑慧敏", generate_password_hash("333333"), None, None, None, None, None, 3),
    (6, "zeng@gmail.com", "曾煜棋", generate_password_hash("444444"), None, None, None, None, None, 4),
    (7, "zehg2@gmail.com", "曾憲章", generate_password_hash("444444"), None, None, None, None, None, 4),
    (8, "crdow@fcu.edu.tw", "竇其仁", generate_password_hash("555555"), None, None, None, None, None, 5),
    (9, "ywang@fcu.edu.tw", "王益文", generate_password_hash("666666"), None, None, None, None, None, 6),
    (10, "chiunghon@gmail.com", "李俊宏", generate_password_hash("666666"), None, None, None, None, None, 6),
    (11, "yang@gmail.com", "楊晴雯", generate_password_hash("777777"), None, None, None, None, None, 7),
    (12, "cai@gmail.com", "蔡明峰", generate_password_hash("777777"), None, None, None, None, None, 7),
    (13, "yjchen@fcu.edu.tw", "陳雅真", generate_password_hash("888888"), None, None, None, None, None, 8),
    (14, "cnhuang@fcu.edu.tw", "黃鎮南", generate_password_hash("888888"), None, None, None, None, None, 8),
    (15, "luo@gmail.com", "羅浩榮", generate_password_hash("999999"), None, None, None, None, None, 9),
    (16, "xie@gmail.com", "謝祥圻", generate_password_hash("999999"), None, None, None, None, None, 9),
]
cur.executemany("INSERT INTO teachers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", teachers)
con.commit()
