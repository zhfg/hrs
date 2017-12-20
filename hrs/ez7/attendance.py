# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import *
from enum import Enum, unique


class Attendance():
    '''
    考勤状态
    1. 上班考勤 
    2. 上班迟到
    3. 上班缺勤
    4. 下班考勤
    5. 下班早退
    6. 下班缺勤
    '''
    def __init__(self, 
            employee_id = None, 
            employee_name = None, 
            att_date = None, 
            att_inttime = None, 
            att_outtime = None, 
            att_state = None):
        self.employee_id = employee_id
        self.employee_name = employee_name   
        self.att_date = att_date   
        self.att_intime = att_intime  
        self.att_outtime = att_outtime    
        self.att_state = att_state  

    def get_att_state(self):
        return self.att_state

    def set_att_state(self, state):
        if state >6 or state < 1:
            raise Exception("state need between 1 and 6")
        self.att_state = state  
