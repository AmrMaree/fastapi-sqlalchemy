import os

DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'postgres')  

if DATABASE_TYPE == 'postgres':
    from app.db.db_pg import Base, engine, get_db
elif DATABASE_TYPE == 'mysql':
    from app.db.db_mysql import Base, engine, get_db
else:
    from app.db.db_sqlite import Base, engine, get_db