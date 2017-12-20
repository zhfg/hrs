#!/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from exceptions import Exception
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
#        Base = automap_base()
#        Base.prepare(self.db_engine, reflect=True)
        self.db_session = Session(self.db_engine)

    def get_all_employees(self):
        return self.db_session.query(Employee).all()

    def get_employee(self, emp_id = None, emp_name = None):
        if emp_id != None:
            employee = self.db_session.query(Employee).filter(Employee.empId == emp_id)
        elif emp_name != None:
            employee = self.db_session.query(Employee).fileter(Employee.empName == emp_name)
        else:
            raise Exception("emp_id or emp_name need given")

    def get_access(self, acc_id="", acc_name=""):
        if acc_id == "" and acc_name == "":
            return self.db_session.query(Access).all()
        if acc_id != "":
            return self.db_session.query(Access).filter(Access.acc_id == acc_id)
        if acc_name != "":
            return self.db_session.query(Access).filter(Access.acc_name == acc_name)

    def get_record(self, employee_id = None, card_id = None, start_time = None, end_time = None, acc_id = None):
        records= self.db_session.query(Record)
 #       import pdb;pdb.set_trace()
        if employee_id != None:
            records = records.filter(Record.employee_id == employee_id)
        if start_time == None:
            start_time = datetime.now()
            start_time = datetime(start_time.year, start_time.month, start_time.day, 0, 0, 59)
#        records = records.filter(Record.access_time >= start_time)

        if end_time == None:
            end_time = datetime.now()
            end_time = datetime(end_time.year, end_time.month, end_time.day, 23, 59, 59)
        records = records.filter(Record.access_time >= start_time,  Record.access_time <= end_time)
#        else:
#            records = records.all()
#        import pdb; pdb.set_trace()
        if acc_id != None:
            records = records.filter(Record.access_id == acc_id)
        return records.all()
    
    def get_attendance(self, employee_id = None, start_time = None, end_time = None, in_or_out = None):
        access_in = ["00A030", "00A031"]
        access_out = ["00A032", "00A033"]
        if not in_or_out:
            acc_ids = access_in
        elif in_or_out == "in":
            acc_ids = access_in
        elif in_or_out == "out":
            acc_ids = access_out
        else:
            raise Exception("in_or_out must be in or out")

        all_records = []
        for acc_id in acc_ids:
            records = self.get_record(employee_id = employee_id, start_time = start_time, end_time = end_time, acc_id = acc_id)
            all_records.extend(records)

        return all_records

    
    def calc_attendance(self, 
            employee_id = None, 
            start_date = date.today(), 
            end_date = date.today()):
        all_employees = self.get_all_employees
        oneday = timedelta(days=1)
        for employee in all_employees:
            start_time = datetime(start_data.year, start_date.month, start_date.day, 0, 0, 0)
            end_time = datetime(end_data.year, end_date.month, end_date.day, 23, 59, 59)
            
            emp_att = Attendance(employee_id = employee.employee_id,
                    employee_name = employee.employee_name)
            emp_att_in = self.get_attendance(
                    employee_id = employee.employee_id, 
                    start_time = start_time, 
                    end_time = end_time, 
                    in_or_ot = "in" )
            emp_att_out = self.get_attendance(
                    employee_id = employee.employee_id, 
                    start_time = start_time, 
                    end_time = end_time, 
                    in_or_ot = "out" )
            
