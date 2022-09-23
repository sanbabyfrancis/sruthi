import sqlite3
conn = sqlite3.connect('userlog.db')
c = conn.cursor()
c.execute("""CREATE TABLE Userlog (
             Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
             Query TEXT,
             Keyword TEXT
                                    )""")
conn.commit()
conn.close()