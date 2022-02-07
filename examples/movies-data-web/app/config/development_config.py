from app.config.base import Base


class DevelopmentConfig(Base):
    # SQLALCHEMY Configuration Keys
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#configuration-keys
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/movie-data-web'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
