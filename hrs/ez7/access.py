# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import *
from enum import Enum, unique

metadata = MetaData()

accType = {'1' : u"门禁", '3' : u'考勤'}

PAccM001 = Table('PAccM001', metadata,
        Column('PAccM0a08', String(10), nullable=False, primary_key=True),
        Column('PAccM0a06', String(1)),
        Column('PAccM0a05', String(length = 40))
        )
Base = declarative_base()

class Access(Base):
    __table__ = PAccM001

    id = PAccM001.c.PAccM0a08
    type = PAccM001.c.PAccM0a06
    name = PAccM001.c.PAccM0a05

    def __repr__(self):
        return "<Access(acc_id=%s, acc_type=%s, acc_name=%s>" % (
                self.accID, self.accType, self.accName.encode('utf-8'))
    
    def list(self, ez7):
        return ez7.db_session.query(Access).all()

    def get(self, ez7, access_id):
        return ez7.db_session.query(Access).filter(Access.id = access_id).first()

