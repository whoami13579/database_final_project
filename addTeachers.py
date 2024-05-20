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
        '''''',
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
        '''''',
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
        '''''',
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
        '''張真誠講座教授，國際電子電機工程師學會會士(IEEE Fellow)、英國電機工程師學會會士(IET Fellow)、中華民國電腦學會會士(CS Fellow)與亞太人工智能學會會士(AAIA Fellow)，並獲選為歐洲科學院（英國）院士和歐洲科學與藝術研究院（奧地利）院士。先後就讀於清華大學和交通大學計算機工程研究所，並以兩年時間榮獲全國首位計算機工程領域國家工學博士，並獲頒國立中正大學名譽工學博士。曾任交通大學副教授，中興大學教授，清華大學教授，中正大學講座教授、工學院院長、教務長、代理校長和教育部顧問室主任等職，並獲邀擔任日本東京大學客座研究員、京都大學客座科學家。

張教授對資訊安全、密碼學與多媒體圖像處理等領域有卓越貢獻，發表學術論文千餘篇、專著38冊，取得美中台專利33項，主持研究計畫百餘項。根據Google Scholar的統計，截至2024年一月共獲引用47,383次， H影響因子為99。2017年8月Guide2Research發布的全球計算機科學學術影響力排名，在一千名頂級科學家，張教授位列全台第一。2021年10月，美國史丹佛大學發佈全球前2%頂尖科學家榜單，張教授在人工智慧與影像處理領域25萬5千餘名科學家中生涯影響力名列全球第189名。張教授曾獲第一屆十大傑出資訊人才獎、資訊榮譽獎章、青年獎章、龍騰十傑獎、傑出工程教授獎、兩屆中山學術著作獎、連續五屆國科會傑出研究獎、東元科技獎、李遠哲傑出人才講座、潘文淵研究傑出獎、美國Journal of Systems and Software期刊全球前十五名頂尖學者獎、美國Pattern Recognition Letters期刊最佳引文獎、國科會傑出特約研究獎、英國IET學會首屆傑出研究獎、2012亞洲資訊安全終身成就獎等。

多年來，張教授應國內外大學及國際會議邀請，發表學術演講千餘場，獲聘北京大學、清華大學、浙江大學、上海交大、華中科大、武漢大學等名校之客座教授、名譽教授和講席教授等。''',
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
        '''''',
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
        '''逢甲大學特約講座教授

曾煜棋教授在無線網路及感測網路方面的貢獻卓著，最著名的研究成果有無線隨意網路的broadcast storm問題和無線感測網路的sensor coverage問題，系列著作已被引用5000次以上。他著有300餘篇論文，被廣泛引用達28,000次以上，根據Google學術搜尋，他的h-index指標達到70，在臺灣工程領域中數一數二，亦曾名列全球無線通訊及網路領域之名人榜。曾教授擁有網通專利二十餘項，成果技轉至中華電信、合勤、宏碁、友訊等知名廠商，並擔任多項國際研討會及頂尖期刊編輯，對臺灣的產業界及學術界貢獻卓著。

曾教授從事之研究表現備受矚目及肯定，獲獎無數，曾獲教育部第23屆國家講座、2018 TWAS Prize in Engineering Sciences、IEEE Fellow、科技部「傑出特約研究員獎」、教育部第58屆學術獎、李國鼎穿石獎、中國電機工程學會傑出電機工程教授獎、有庠科技講座、三次科技部傑出研究獎及第二十屆東元科技獎等獎項，為物聯網、行動通訊、AI及智慧服務領域中的佼佼者。

曾煜棋教授並熱心服務，現任國立陽明交通大學智慧科學暨綠能學院創院院長及人工智慧普適研究中心主任，曾任資訊學院院長、資訊工程學系系主任、交大工研院聯合研發中心執行長。曾教授帶領其研究團隊，兢兢業業探求真理，並將學術落實於實務中，對國內學術界之奉獻不遺餘力。''',
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
        '''曾憲章博士於1970 年畢業於國立臺灣大學電機系，1976 年畢業於美國加州大學獲電腦博士學位。在美期間服務於高科技中心-矽谷的PARC(XEROX 的研究中心)，1980 年回臺灣，在新竹科學園區創立全友電腦(MICROTEK)，嗣於民國77 年上市，是園區第1 家上市的高科技公司，他們的掃描器市場佔全世界第1 位。曾博士不僅是高科技企業的傑出經營者，也是人才培訓的熱愛者，培育了近百位高科技企業經營管理人才。 曾博士是美國百人會(Committeeof100) 的理事， 也是美國玉山(MonteJade)科技協會的創辦人之一，協助中美兩岸三地華人創業。美國益客(ECO)環保基金會創辦人，在北京、四川、雲南等地大量種樹造林。 曾博士曾擔任新竹科學園區鼎賀公司副董事長及元太、TCL 等公司董事，從事高科技企業的經營及策略聯盟，並兼任新竹清華大學校長特别顧問及EMBA 教授、加拿大Alberta 大學客座教授、香港城市大學客座教授、北京清華大學總裁培訓班教授、天津南開大學、四川大學及成都電子科技大學客座教授。同時亦擔任天津市政府經濟顧問、天津泰達經濟技術開發區(TEDA)高级顧問，兼任四川郎博西部中小企業研究院名譽院長。 曾博士由於在高科技產業的創新性工作及領導力表現，以及對於高科技人才培育的特殊貢獻， 榮獲美洲中國工程師協會(ChineseInstituteofEngineering，USA)頒發“2004 年，傑出成就獎”。2005年獲聘加拿大國家納米研究中心(NINT)海外董事；2006 年擔任美國“贈與亞洲基金會”理事；2008 年榮獲中國政府頒發“國家友誼獎”，聲望崇隆。''',
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
        '''''',
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
        '''''',
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
        '''畢業於國立中正大學電機工程系博士班;主要研究領域為人工智慧與軟體工程，特別是人工智慧技術於軟體工程與財金領域之應用。在校內講授計算機結構學及資料結構等課程。曾擔任台灣軟體工程學會的秘書長及理事，協助推廣軟體工程之相關技術。在教學上認為教學是一個溝通的過程，強調理論與實務並行，能學以致用為目標。在專業授課及演講之外,亦曾應邀至各級學校或政府及民間單位提供生命教育，親子講座，武術健身等相關演講逾數百場。''',
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
        '''''',
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
        '''''',
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
        '''''',
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
        '''''',
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
        '''''',
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
        '''''',
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
