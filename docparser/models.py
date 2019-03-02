from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'ekids',
    'password': 'ekids',
    'database': 'chado_content'
}

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**DATABASE))


def create_product_doc_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class ProductDOC(DeclarativeBase):
    __tablename__ = 'parsers_productdoc'

    id = Column(Integer, primary_key=True)
    code_1c = Column('code_1c', String)
    url = Column('url', String)

    def __repr__(self):
        return "<ProductDOC(code='{0}')>".format(self.code_1c)