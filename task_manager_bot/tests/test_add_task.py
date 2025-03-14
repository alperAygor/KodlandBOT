import pytest
import db
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
from controllers.task_controller import AddTask

@pytest.mark.asyncio
async def test_complete_task():
    logging.info("Testing Add Function")
    cursor=db.GetCursor()
    conn=db.GetConn()
    assert conn is not None, "Database connection is None!"
    assert cursor is not None, "Cursor is None!"
    logging.info("Database connection is initialized")
    
    await AddTask(cursor,conn,"task1")
    
    cursor.execute("SELECT description FROM tasks")
    task_descriptions = cursor.fetchall()
    logging.info("Checking Tasks...")
    assert task_descriptions, "No tasks found in the database!"
    logging.info("Tasks Found in Database")
    founded=False
    for i, description in enumerate(task_descriptions, start=1):
        if(description[0]=="task1"):
            founded=True
            break
    assert founded  ,"Cannot Found"
    
    logging.info("Added Task is Found")
    logging.info("Test Passed\n\n")
