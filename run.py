import multiprocessing

from config import TOKEN
from bot import client
from app import create_app
from settings import Settings

app = create_app(Settings)

if __name__ == "__main__":
    api = multiprocessing.Process(target=app, name='api')
    bot = multiprocessing.Process(target=client, args=(TOKEN))

    api.start()
    # bot.start()
