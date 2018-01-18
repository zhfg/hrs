#!/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
#from exceptions import Exception
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from employee import *
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, date, timedelta
from access import *
from record import *
from attendance import *
db_types = ["mssql"]

jobState = {'001' : u'在职', '002' : u'离职', '003' : u'内部调动'}

class Error(Exception):
    def __init__(self, err_str=""):
        self.err_str = err_str

    def __str__(self):
        return repr(self.err_str)

class EZ7:
    def __init__(self, db_type = "mysql",
            db_host = "localhost", 
            db_port = 1433, 
            db_user = "sa", 
            db_passwd = "", 
            db_name = "eZ7"):
        self.db_type = db_type
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name
        self.init_db_session()

        self.employee = Employee()

    def init_db_session(self):
        str_connection = ""
        if self.db_type not in ["mssql",]: 
        #:warning "postgres", "sqlite", "mysql"]
            raise Error("Error db type")

        if self.db_type == "mssql":
            self.db_package = "pymssql"
        str_connection = "%s+%s://%s:%s@%s:%s/%s" % (
                self.db_type, 
                self.db_package, 
                self.db_user, 
                self.db_passwd, 
                self.db_host, 
                self.db_port, 
                self.db_name)
        self.db_engine = create_engine(str_connection)
        self.db_session = Session(self.db_engine)
