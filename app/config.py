class Config(object):
    NAME = 'Default'
    DEBUG = False
    TESTING = False
    TEST_STRING = 'This is the default configuration'

class Development(Config):
    NAME = 'Development'
    DEBUG = True
    TEST_STRING = 'This is the development configuration'

class Production(Config):
    NAME = 'Production'
    TEST_STRING = 'This is the production configuration'

class Test(Config):
    NAME = 'test'
    DEBUG = False
    TESTING = True


EXPORT_CONFIGS = [
    Development,
    Production,
    Test
]

config_by_name = {cfg.NAME: cfg for cfg in EXPORT_CONFIGS}