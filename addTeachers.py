import sqlite3
from werkzeug.security import generate_password_hash

con = sqlite3.connect("instance/database.db")
cur = con.cursor()

teachers = [
    (
        1,
        "leejs@fcu.edu.tw",
        "李榮三",
        generate_password_hash("111111"),
        None,
        None,
        None,
        None,
        """無線通訊
Wireless Communications
資訊安全
Information Security
電子商務
E-Commerce
密碼學
Cryptography
數位影像處理
Image Processing
區塊鏈技術與應用
Blockchain technique and its application""",
        "中正大學 資訊工程學系 博士\n中正大學 資訊工程學系 學士",
        1,
    ),
    (
        2,
        "tcyang@fcu.edu.tw",
        "楊濬中",
        generate_password_hash("222222"),
        None,
        None,
        None,
        None,
        """計算機結構
Computer Architecture
容錯計算
Fault-Tolerant Computing
通訊系統
Communication Systems""",
        "美國伊利諾理工學院 計算機科學系 博士\n美國華盛頓州立大學 計算機科學系 碩士\n國立成功大學 電機工程系 學士",
        2,
    ),
    (
        3,
        "acliu@fcu.edu.tw",
        "劉安之",
        generate_password_hash("222222"),
        None,
        None,
        None,
        None,
        '''網路管理
Network Management
分散式系統
Distributed System
資料庫系統
Database System''',
        "美國伊利諾大學芝加哥分校 電機電腦 博士\n國立交通大學 計算機工程 碩士\n國立交通大學 控制工程系 學士",
        2,
    ),
    (
        4,
        "alan3c@gmail.com",
        "張真誠",
        generate_password_hash("333333"),
        None,
        None,
        None,
        None,
        '''資料庫設計
Database Design
電子商務安全
E-Business Security
電子多媒體影像技術
Electronic Imaging Techniques
電腦密碼學
Computer Cryptography
圖像與信號處理
Image and Signal Processing
信息取證與安全
Information Forensics and Security
深度學習
Deep Learning''',
        "1980-09-01 ~ 1982-06-30 國立交通大學 計算機工程學系 博士\n1977-09-01 ~ 1979-06-30 國立清華大學 計算機管理決策研究所 碩士\n1973-09-01 ~ 1977-06-30 國立清華大學 應用數學系 學士",
        3,
    ),
    (
        5,
        "wheyming_song@yahoo.com",
        "桑慧敏",
        generate_password_hash("333333"),
        None,
        None,
        None,
        None,
        '''青光眼預測分析
太陽能與半導體製程品質管制與可靠度
電力節能之最佳設計
機率統計與模擬理論與應用
系統思維''',
        "美國普渡大學 工業工程學系 博士",
        3,
    ),
    (
        6,
        "zeng@gmail.com",
        "曾煜棋",
        generate_password_hash("444444"),
        None,
        None,
        None,
        None,
        '''物聯網
Internet of Things
5G行動科技
5G Mobile Technology
人工智慧服務
AI Service''',
        "美國俄亥俄州立大學 資訊科學系 博士\n美國俄亥俄州立大學 資訊科學系 博士\n國立清華大學 資訊科學系 碩士\n國立清華大學 資訊科學系 碩士\n國立台灣大學 資訊工程學系 學士\n國立台灣大學 資訊工程學系 學士",
        4,
    ),
    (
        7,
        "zehg2@gmail.com",
        "曾憲章",
        generate_password_hash("444444"),
        None,
        None,
        None,
        None,
        '''''',
        "美國加州大學洛杉磯分校(UCLA) 電子計算機 博士\n美國加州大學洛杉磯分校 電子計算機 碩士\n台灣大學 電機系 學士",
        4,
    ),
    (
        8,
        "crdow@fcu.edu.tw",
        "竇其仁",
        generate_password_hash("555555"),
        None,
        None,
        None,
        None,
        '''行動計算
Mobile Computing
車載網路
Vehicular Ad Hoc Networks
智慧聯網
AIoT
雲端計算
Cloud Computing
學習科技
Learning Technology''',
        "美國匹茲堡大學 電腦科學 博士\n美國匹茲堡大學 電腦科學 碩士\n國立交通大學 資訊工程 碩士\n國立交通大學 資訊工程 學士",
        5,
    ),
    (
        9,
        "ywang@fcu.edu.tw",
        "王益文",
        generate_password_hash("666666"),
        None,
        None,
        None,
        None,
        '''嵌入式系統設計
Embedded System Design
VLSI系統設計
VLSI Design
類神經網路
Neural Network''',
        "美國密西根州立大學 電機工程學系 博士\n美國密西根州立大學 電機工程學系 碩士\n國立交通大學 控制工程 學士",
        6,
    ),
    (
        10,
        "chiunghon@gmail.com",
        "李俊宏",
        generate_password_hash("666666"),
        None,
        None,
        None,
        None,
        '''人工智慧
Artificial Intelligence
智慧代理人
Intelligent Agent
軟體工程
Software Engineering
模糊時間序列
Fuzzy Time Series''',
        "國立中正大學 電機工程研究所 博士\n國立中正大學 電機工程研究所 碩士\n國立台灣工業技術學院 電子工程技術系 學士",
        6,
    ),
    (
        11,
        "yang@gmail.com",
        "楊晴雯",
        generate_password_hash("777777"),
        None,
        None,
        None,
        None,
        '''資料庫設計
Database Design
影像處理
Imege Processing
醫療資訊
Medical Informatics
無線網路應用
Wireless Network Application
醫學影像儲傳系統
PACS''',
        "成功大學 電機所計算機組 博士\n成功大學 資訊工程學系 碩士",
        7,
    ),
    (
        12,
        "cai@gmail.com",
        "蔡明峰",
        generate_password_hash("777777"),
        None,
        None,
        None,
        None,
        '''嵌入式系統
Embedded System
作業系統
Operating System
車載資通訊系統整合平台
Telematics System Integration Platform
多媒體訊號處理
Multimedia Signal Processing
無線通訊系統
Wireless Communication Systems''',
        "國立成功大學 電腦與通訊工程研究所 博士\n國立成功大學 電腦與通訊工程研究所 碩士\n國立台灣科技大學 電機工程學系 學士",
        7,
    ),
    (
        13,
        "yjchen@fcu.edu.tw",
        "陳雅真",
        generate_password_hash("888888"),
        None,
        None,
        None,
        None,
        None,
        None,
        8,
    ),
    (
        14,
        "cnhuang@fcu.edu.tw",
        "黃鎮南",
        generate_password_hash("888888"),
        None,
        None,
        None,
        None,
        None,
        None,
        8,
    ),
    (
        15,
        "luo@gmail.com",
        "羅浩榮",
        generate_password_hash("999999"),
        None,
        None,
        None,
        None,
        '''平行處理
Parallel Processing
高速運算
High-speed Computing''',
        "日本國立北海道大學 計算機工程 博士\n國立成功大學 電機工程研究所 碩士\n海軍機械學校 電機系 學士",
        9,
    ),
    (
        16,
        "xie@gmail.com",
        "謝祥圻",
        generate_password_hash("999999"),
        None,
        None,
        None,
        None,
        '''決策支援系統設計
Decision Support System Design
數據通信與網路
Data Communications & Netwroking
作業研究
Operations Research
高等作業研究
Advanced Operations Research''',
        "美國德瑞克大學 資訊教育 博士\n美國蘭塞拉爾理工學院 管理科學 碩士",
        9,
    ),
]
cur.executemany(
    "INSERT INTO teachers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", teachers
)
con.commit()
