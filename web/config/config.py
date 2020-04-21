class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = 'mysql'

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return 'mysql://{user}:{password}@{server}/{database}'.format(user='root', password='root', server='mysql', database='poker')
        # return 'mysql://root:root@mysql/poker'


class DevelopmentConfig(Config):
    DEBUG = True
