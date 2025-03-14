import sqlite3
conn=None
cursor=None
def ExecuteDatabase():
    global conn, cursor
    conn=sqlite3.connect("db/database.db")

    cursor=conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        isCompleted INTEGER
    )
    ''')
    

    conn.commit()
def GetCursor():
    return cursor

def GetConn():
    return conn