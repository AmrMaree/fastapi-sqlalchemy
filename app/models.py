from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db_pg import Base

class User(Base):
        __tablename__='users'
        id = Column('id', Integer(), primary_key=True, index=True)
        name = Column('name', String(50), nullable=False)
        email = Column('email', String(50), unique=True, index=True, nullable=False)
        password = Column('password', String(100),nullable=False)
        salt = Column('salt', String(100),nullable=False)

        posts = relationship('Post', backref='user', cascade='all, delete-orphan')
        comments = relationship('Comment', backref='user', cascade='all, delete-orphan')

        def __repr__(self):
                return "User(id={self.id},name={self.name},email={self.email},password={self.password},salt={self.salt})".format(self=self)
                                                        
    
class Post(Base):
        __tablename__= 'posts'
        id = Column('id', Integer(), primary_key=True, index=True)
        title = Column('title', String(50), nullable=False)
        content = Column('content', String(50), nullable=False)
        user_id = Column('user_id', ForeignKey('users.id'))  

        comments = relationship('Comment', backref='post', cascade='all, delete-orphan')        
        
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
           
    