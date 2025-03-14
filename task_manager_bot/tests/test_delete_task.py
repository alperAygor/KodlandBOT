import pytest
import db
import asyncio
from controllers.task_controller import AddTask,DeleteTask

import logging

logging.basicConfig(level=logging.INFO)
@pytest.mark.asyncio
async def test_complete_task():
    logging.info("Testing Delete Function")
    
    cursor=db.GetCursor()
    conn=db.GetConn()
    
    await AddTask(cursor,conn,"task3")
    logging.info("Task Added")
    cursor.execute("SELECT id,description FROM tasks")
    tasks = cursor.fetchall()
    logging.info("Checking Tasks...")
    assert tasks, "No tasks found in the database!"
    logging.info("Tasks Found in Database")
    task_id = None
    founded=False
    for i,task in enumerate(tasks,start=1):
        if task[1] == "task3":  # description task[1] içinde
            task_id = task[0]   # id task[0] içinde
            founded = True
            break  # Döngüyü erkenden durdur
    assert founded  ,"Cannot Found"
    await DeleteTask(cursor,conn,task_id)
    
    cursor.execute("SELECT isCompleted FROM tasks WHERE id = ?", (task_id,))
    result = cursor.fetchone()
    
    assert result is None,"Cannot Deleted Task"
    
    logging.info("Test Passed\n\n")
