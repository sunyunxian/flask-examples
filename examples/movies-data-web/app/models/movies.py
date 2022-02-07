from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movies(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=50), nullable=False)
    author = Column(String(length=30), default='Unknown author')
    binding = Column(String(length=30), default='Unknown binding')
    publisher = Column(String(length=30), default='Unknown publisher')
    page = Column(Integer, default='Unknown page')
    pubdate = Column(String(length=20))
    isbn = Column(String(length=8), nullable=False, unique=True)
    summary = Column(String(length=1000), default='Unknown summary')
    image = Column(String(length=100))

    def __repr__(self) -> str:
        return f'{self.id}: {self.title}'

    def foo(self):
        pass
