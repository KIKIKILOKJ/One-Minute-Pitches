import os
from instance.config import SECRET_KEY

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL')
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://peter:abcdef@localhost/pitchess'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}