from config import data


class Settings(object):
    DEBUG = False

    HOST = '0.0.0.0'
    PORT = '8080'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}'.format(
        user=data['user'],
        password=data['password'],
        host=data['host'],
        database=data['database']
    )
