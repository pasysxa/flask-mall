class DefaultConfig:
    BCRYPT_LEVEL = 11
    DEBUG = False
    TESTING = False
    SECRET_KEY = '~k(&%I(H&&D((&"!""'
    DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(DefaultConfig):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class TestingConfig(DefaultConfig):
    TESTING = True