
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sevices.models import User


class UserHandler:
    def __init__(self):
        self.engine = create_engine('sqlite:///remcuauser.db', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def check(self , username , password):
        user = self.session.query(User).filter_by(username=username, password=password).first()
        if user is None:
            return False
        else:
            return True

    def add_user( self , username, password):
        new_user = User(username=username, password=password)
        self.session.add(new_user)
        self.session.commit()



