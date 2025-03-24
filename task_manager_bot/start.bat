@echo off
python -m pip install --upgrade pip

if not exist "requirements.txt" (
    echo discord.py > requirements.txt
    echo python-dotenv >> requirements.txt
    echo aiohttp >> requirements.txt
    echo requests >> requirements.txt
    echo pytest >> requirements.txt
    echo pytest-asyncio >> requirements.txt
    echo cryptography >> requirements.txt
)

:: Bağımlılıkları yükle
python -m pip install -r requirements.txt
cls
python bot.py 
pause

