import os


class Config:
    '''General configuration parent class'''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=0cff81b85884415aa6f77fb081c448f8'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


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