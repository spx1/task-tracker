class Config(object):
    DEBUG = False
    TESTING = False
    TEST_STRING = 'This is the default configuration'

class Development(Config):
    DEBUG = True
    TEST_STRING = 'This is the development configuration'

class Production(Config):
    TEST_STRING = 'This is the production configuration'