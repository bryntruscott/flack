import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '51f52814-0071-11e6-a247-000ec6c2372c')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'mysql+pymysql://flack:flack@192.168.2.125/flack')
        # 'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'db.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REQUEST_STATS_WINDOW = 15
    CELERY_CONFIG = {}
    SOCKETIO_MESSAGE_QUEUE = os.environ.get('CELERY_BROKER_URL', 'redis://192.168.2.125')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    CELERY_CONFIG = {'CELERY_ALWAYS_EAGER': True}
    SOCKETIO_MESSAGE_QUEUE = None


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
