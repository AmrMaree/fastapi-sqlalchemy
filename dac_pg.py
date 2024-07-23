from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql+psycopg2://postgres:123@localhost:5433/posts'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()