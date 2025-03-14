import pytest
import db
import asyncio
from controllers.task_controller import ShowTasks,AddTask
import logging

logging.basicConfig(level=logging.INFO)
@pytest.mark.asyncio
async def test_complete_task():
    logging.info("Testing Get Function")
    
    cursor=db.GetCursor()
    conn=db.GetConn()
    
    await AddTask(cursor,conn,"Task4")
    logging.info("Task Added")
    tasks=await ShowTasks(cursor)
    assert tasks is not None ,"Tasks Not Found"
    
    logging.info("Test Passed\n\n")
