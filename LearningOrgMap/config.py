class Config(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TITLE_PREFIX = 'DEV'

class TestingConfig(Config):
    TESTING = True