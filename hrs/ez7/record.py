# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import *
from enum import Enum, unique

metadata = MetaData()

PAccM301 = Table('PAccM301', metadata, 
        Column('PAccM3a00', String(3), primary_key=True),
        Column('PAccM3a01', DateTime, primary_key=True),
        Column('PAccM3a02', String(20), primary_key=True),
        Column('PAccM3a03', String(10), primary_key=True),
        Column('PAccM3a04', String(10)),
        Column('PAccM3a05', String(4)),
        Column('PAccM3a06', DateTime),
        Column('PAccM3a07', DateTime)
        )
Base = declarative_base()
class Record(Base):
    __table__ = PAccM301 

    compay_id = PAccM301.c.PAccM3a00
    access_time = PAccM301.c.PAccM3a01
    card_id = PAccM301.c.PAccM3a02
    access_id = PAccM301.c.PAccM3a03
    employee_id = PAccM301.c.PAccM3a04

     
