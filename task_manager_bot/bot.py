import discord,db
from discord.ext import commands
from controllers.task_controller import AddTask, DeleteTask, ShowTasks, CompleteTask
from cryptography.fernet import Fernet

# Botu başlatma fonksiyonu
with open("secret.key", "rb") as key_file:
    key = key_file.read()

# Fernet şifreleyicisini oluştur
fernet = Fernet(key)

# Şifreli token'ı dosyadan oku
with open("encrypted_token.txt", "rb") as enc_file:
    encrypted_token = enc_file.read()

# Token'ı çöz
token = fernet.decrypt(encrypted_token).decode()
db.ExecuteDatabase()
conn = db.GetConn()
cursor = db.GetCursor()




intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def add_task(ctx, *, description: str):
    await AddTask(cursor, conn, description)
    await ctx.send(f"Task added! {description} To list all tasks use !show_tasks")

@bot.command()
async def complete_task(ctx, *, id: str):
    await CompleteTask(cursor, conn, id)
    await ctx.send(f"Task {id} completed!")

@bot.command()
async def show_tasks(ctx):
    tasks = await ShowTasks(cursor)
    if tasks:
        for i, task in enumerate(tasks, start=1):
            isCompleted = "Yes" if task[2] == 1 else "No"
            await ctx.send(f"id:{task[0]}: {task[1]} --- Completed: {isCompleted}")
    else:
        await ctx.send("No tasks found.")

@bot.command()
async def delete_task(ctx, *, id: str):
    await DeleteTask(cursor, conn, id)
    await ctx.send(f"Task {id} deleted")

if __name__ == "__main__":
    bot.run(token)