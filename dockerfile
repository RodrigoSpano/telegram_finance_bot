FROM python:3.9

COPY telegram_bot.py ./telegram_bot.py
COPY gsheets.py ./gsheets.py
COPY credentials.json ./credentials.json

RUN pip install pyTelegramBotAPI python-dotenv gspread oauth2client

#EXPOSE 1001

CMD ["python", "./telegram_bot.py"]
