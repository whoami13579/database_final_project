import sqlite3

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

external_experiences = [
    (1, None , None , None ,"朝陽科技大學 校長", 2),
    (2, None , None , None ,"僑光技術學院 校長", 2),
    (3, None , None , None ,"工業技術研究院 電腦與通訊研究所 所長", 2),
    (4, None , None , None ,"教育部 研究員兼領域召集人", 3),
    (5, None , None , None ,"法鼓大學 籌備處 主任", 3),
    (6, None , None , None ,"美國伊利諾大學 工學院 助理教授", 3),
    (7, None , None , None ,"2018-08-01 ~ 迄今 朝陽科技大學 資訊系 榮譽特聘講座教授", 4),
    (8, None , None , None ,"2018-02-01 ~ 迄今 國立金門大學 兼任講座教授", 4),
    (9, None , None , None ,"2016-11-01 ~ 迄今 國立東華大學 資工系 榮譽教授", 4),
    (10, None , None , None ,"國立清華大學 工業工程與工程管理學系 特聘教授", 5),
    (11, None , None , None ,"UC Davis, USA Medical School 客座教授", 5),
    (12, None , None , None ,"U.C. Berkeley Department of Electrical Engineering and Computer Science 客座教授", 5),
    (13, None , None , None ,"國立陽明交通大學 智慧科學暨綠能學院 創院院長", 6),
    (14, None , None , None ,"國立陽明交通大學 智慧科學暨綠能學院 創院院長", 6),
    (15, None , None , None ,"國立陽明交通大學 工智慧普適研究中心 主任", 6),
    (16, None , None , None ,"亞洲大學 資訊工程學系 榮譽講座教", 7),
    (17, None , None , None ,"曉龍基金會 董事長", 7),
    (18, None , None , None ,"私立大華工商專科學校 資管科 副教授", 8),
    (19, None , None , None ,"Siemens 普林斯頓研發中心 研究助理", 8),
    (20, None , None , None ,"美國匹茲堡大學 經濟學系 程式設計師", 8),
    (21, None , None , None ,"美國明尼蘇答大學 電腦工程系 助理教授", 9),
    (22, None , None , None ,"美國密西根州立大學 電機系 研究助理", 9),
    (23, None , None , None ,"南華大學 資訊工程學系 副教授", 10),
    (24, None , None , None ,"南華大學 資訊工程學系 助理教授", 10),
    (25, None , None , None ,"中州技術學院 資訊工程學系 助理教授", 10),
    (26, None , None , None ,"黑瘋科技股份有限公司 董事長", 11),
    (27, None , None , None ,"乙太資訊股份有限公司 總經理", 11),
    (28, None , None , None ,"台中榮民總醫院 資訊室 主任", 11),
    (29, None , None , None ,"國立聯合大學 電子工程學系 教授", 12),
    (30, None , None , None ,"國立聯合大學 教授", 12),
    (31, None , None , None ,"國立聯合大學 電子工程學系 教授", 12),
]
cur.executemany("INSERT INTO external_experiences VALUES(?, ?, ?, ?, ?, ?)", external_experiences)
con.commit()
