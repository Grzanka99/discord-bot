import threading

from config import TOKEN
from bot import client
from app import create_app
from settings import Settings

app = create_app(Settings)


def run_api():
    app.run()


def run_bot():
    client.run(TOKEN)

if __name__ == "__main__":
    api = threading.Thread(target=run_api)
    bot = threading.Thread(target=run_bot)

    api.start()
    bot.run()
