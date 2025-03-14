async def AddTask(cursor,conn,description):
    cursor.execute("INSERT INTO tasks (description,isCompleted) VALUES (?, ?)", (description,0))
    conn.commit()

async def DeleteTask(cursor,conn,id):
    cursor.execute("DELETE FROM tasks WHERE id = ?",(id,))
    conn.commit()
    
async def ShowTasks(cursor):
    cursor.execute("SELECT id,description,isCompleted FROM tasks")
    tasks = cursor.fetchall()
    return tasks
    
    
async def CompleteTask(cursor,conn,id):
    cursor.execute("UPDATE tasks SET isCompleted = 1 WHERE id = ?", (id,))
    conn.commit()
    
    