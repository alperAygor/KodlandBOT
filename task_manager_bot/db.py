import sqlite3
conn=None
cursor=None
# db.py dosyasında bu şekilde değiştirin
def ExecuteDatabase():
    import os
    if not os.path.exists('db'):
        os.makedirs('db')
    db_path = os.path.join(os.path.dirname(__file__), 'db/database.db')
    global conn, cursor
    conn=sqlite3.connect(db_path)

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