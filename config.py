import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ex-2.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ex-2-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ex-2-admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'User1234567'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ex2bloblaccount'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ladPGiEGInQ2C5LIl86IHSIr4/VIlV689+HnrTvDPnZiL8jJ5bj5yQZ2rr+TICAXlf/mE/ybyaPt+AStiTj58Q=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'