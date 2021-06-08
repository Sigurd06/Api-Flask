class Config(object):
    SECRET_KEY = 'Se:cR:E:cT::K:e:Y'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/db_trello_clone'

config = {
    'development': DevelopmentConfig,
    
    'default': DevelopmentConfig
}