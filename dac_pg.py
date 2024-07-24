from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://postgres:123@localhost:5433/posts'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()



Base = declarative_base()

class User(Base):
        __tablename__='users'
        id = Column('id', Integer(), primary_key=True, index=True)
        name = Column('name', String(50), nullable=False)
        email = Column('email', String(50), unique=True, index=True, nullable=False)
        password = Column('password', String(50),nullable=False)
        salt = Column('salt', String(50),nullable=False)

        posts = relationship('Post', backref='user')
        comments = relationship('Comment', backref='user')

        def __repr__(self):
                return "User(id={self.id},name={self.name},email={self.email},password={self.password},salt={self.salt})".format(self=self)
                                                        
    
class Post(Base):
        __tablename__= 'posts'
        id = Column('id', Integer(), primary_key=True, index=True)
        title = Column('title', String(50), nullable=False)
        content = Column('content', String(50), nullable=False)
        user_id = Column('user_id', ForeignKey('users.id'))  

        comments = relationship('Comment', backref='post')        
        
        def __repr__(self):
                return "Post(id={self.id},title={self.title},content={self.content},user_id={self.user_id})".format(self=self)

class Comment(Base):
           __tablename__= 'comments'
           id = Column('id', Integer(), primary_key=True, index=True)
           content = Column('content', String(50), nullable=False)
           post_id = Column('post_id',ForeignKey('posts.id'))
           user_id = Column('user_id', ForeignKey('users.id')) 

           def __repr__(self):
                return "Comment(id={self.id},content={self.content},post_id={self.post_id},user_id={self.user_id})".format(self=self)
           
    
Base.metadata.create_all(engine)