from app.config.base import Base

class TestingConfig(Base):
    # DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True