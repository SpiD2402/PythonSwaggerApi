from os import getenv
from datetime import timedelta


class BaseConfig:
    SQLALCHEMY_DATABASE_URI=getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY=getenv('JWT_SECRET')
    
    
class DevelopmentConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(hours=3)
    

class ProductionConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(hours=1)


environment={
    
    'development':DevelopmentConfig,
    'production':ProductionConfig
    
}