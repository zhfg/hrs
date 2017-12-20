#!/bin/env python
# -*- coding:utf-8 -*-

from ez7 import *
from datetime import date, datetime
if __name__ == '__main__':
    ez7 = EZ7(db_type="mssql", 
            db_host="192.168.88.225", 
            db_port="1433", 
            db_user="hrs", 
            db_passwd="hrs123456",
            db_name="eZ7")

    acc = ez7.get_access()
    for item in acc:
        print(item.id, item.name)
#    all = ez7.get_employee(emp_id="C0001")
#    for item in all:
#        state = jobState[item.jobState]
#        print("%s, %s, %s" % (item.empId, item.empName, state))
#    all_records = []
#    records = ez7.get_record(acc_id = "00A030")
#    all_records.extend(records)
#    records = ez7.get_record(acc_id = "00A031")
#    all_records.extend(records)
#    records = ez7.get_record()
#    print(len(records))
#    print(len(all_records))
    start_time = datetime(2017, 12, 01, 0, 0, 0)
    end_time = datetime(2017, 12, 15, 0, 0, 0)
    all_records = ez7.get_attendance(start_time = start_time, end_time = end_time, in_or_out = "out")
    print(len(all_records))
