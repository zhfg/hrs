# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import *
from enum import Enum, unique

#jobState = {'001':'在职', '002':'离职', '003':'内部调动'}
#@unique
#class jobState(Enum):
#    '001' = '在职'
#    '002' = '离职'
#    '003' = '内部调动'

metadata = MetaData()

PHumM001 = Table('PHumM001', metadata,
        Column('PHumM0a00', Integer, nullable=False, primary_key=True),  #compay_id
        Column('PHumM0a01', String(10), nullable=False, primary_key=True),  #id
        Column('PHumM0a02', String(20)), #nameerror
        Column('PHumM0a39', String(20)),
        Column('PHumM0a17', String(3))  #job_state
        )
Base = declarative_base()

class Employee(Base):
    __table__ = PHumM001

    compay_id = PHumM001.c.PHumM0a00
    id = PHumM001.c.PHumM0a01
    name = PHumM001.c.PHumM0a02
    card_id = PHumM001.c.PHumM0a39
    jobState = PHumM001.c.PHumM0a17


