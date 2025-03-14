import discord
from discord.ext import commands
import db
from controllers.task_controller import AddTask,DeleteTask,ShowTasks,CompleteTask

db.ExecuteDatabase()
conn=db.GetConn()
cursor=db.GetCursor()

#Token Reading

token="MTM1MDA4NjY1ODMyNTg3MjczMA.GrdkTq.HcI9VzqVZGR09cQ12_0BXsXJLqqbkAdyBA1-Ao"
#Discord Tokenı algıladı ve kendi kendine iptal etti 
#normalde token token.txt dosyasından okunuyordu kodu değiştirdim
#SHA256 gibi bir algoritma kullanmak istemedim 
#eğer çalışmazsa muhtemelen token auth hatasından dolayıdır

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


#Adding Task
@bot.command()
async def add_task(ctx,*,description:str):
    await AddTask(cursor,conn,description)
    await ctx.send(f"Task added! {description} To list all tasks use !show_tasks")

#Marking tasks as a completed for id
@bot.command()
async def complete_task(ctx,*,id:str):
    await CompleteTask(cursor,conn,id)
    await ctx.send(f"Task {id} completed!")
  
      
#showing all tasks
@bot.command()
async def show_tasks(ctx):
    tasks=await ShowTasks(cursor)
    if tasks:
        for i, task in enumerate(tasks, start=1):
            isCompleted = "Yes" if task[2] == 1 else "No"
            await ctx.send(f"id:{task[0]}: {task[1]} --- Completed: {isCompleted}")
    else:
        await ctx.send("No tasks found.")

#deleting task for id
@bot.command()
async def delete_task(ctx,*,id:str):
    await DeleteTask(cursor,conn,id)
    await ctx.send(f"Task {id} deleted")

bot.run(token)
