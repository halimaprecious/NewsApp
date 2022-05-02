import os


class Config:
    '''General configuration parent class'''
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/articles/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KAY')


class ProdConfig(Config):
    '''production config of child class'''
    pass


class DevConfig(Config):
    '''Development configuration child class'''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig   
}