import pytest
import db
import asyncio
from controllers.task_controller import CompleteTask,AddTask
import logging

logging.basicConfig(level=logging.INFO)
@pytest.mark.asyncio
async def test_complete_task():
    logging.info("Testing Complete Function")
    
    # Database bağlantısını çalıştır
    cursor = db.GetCursor()
    conn = db.GetConn()
    
    await AddTask(cursor,conn,"task2")
    # Veritabanındaki görevleri kontrol et
    cursor.execute("SELECT id,description FROM tasks")
    tasks = cursor.fetchall()

    logging.info("Checking Tasks...")
    assert tasks, "No tasks found in the database!"

    logging.info("Tasks Found in Database")
    founded = False
    task_id = None

    for i,task in enumerate(tasks, start=1):
        if task[1] == "task2":  # description task[1] içinde
            task_id = task[0]   # id task[0] içinde
            founded = True
            break  # Döngüyü erkenden durdur

    assert founded, "Task with description 'task2' not found in the database!"
    logging.info(f"Task '{task_id}' is Found")

    # Tamamlama fonksiyonunu test et
    await CompleteTask(cursor, conn, task_id)

    # Güncellenmiş durumu kontrol et
    cursor.execute("SELECT isCompleted FROM tasks WHERE id = ?", (task_id,))
    result = cursor.fetchone()

    assert result is not None, "Task not found after update!"
    assert result[0] == 1, f"Task {task_id} is not marked as completed!"

    logging.info("Test Passed\n\n")
