from sqlalchemy.orm import Session
from app.dac.dac import dac

class search_svc:
    def __init__(self):
        self.dac = dac()

    def search_users(self, db : Session, search_query : str):
        return self.dac.search_users(db, search_query)

    def search_posts(self, db : Session, search_query : str):
        return self.dac.search_posts(db, search_query)