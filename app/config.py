class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=c7e4aad3be1347a9aab0ecd2b4c850f5'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey=c7e4aad3be1347a9aab0ecd2b4c850f5'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True