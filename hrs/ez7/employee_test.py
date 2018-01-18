#!/bin/env python
# -*- coding: utf-8 -*-

import unittest
from employee import *
from ez7 import *

class TestEmployeeMethods(unittest.TestCase):
    def test_list(self):
        ez = EZ7(
            db_host = "221.224.194.203",
            db_port = 2433,
            db_type = "mssql",
            db_user = "hrs",
            db_passwd = "hrs123456",
            db_name = "eZ7"
            )
        
        e = Employee()
        employees = e.list(ez.db_session)
        for item in employees:
            print(item.id)

    def test_get(self):
        ez = EZ7(
            db_host = "221.224.194.203",
            db_port = 2433,
            db_type = "mssql",
            db_user = "hrs",
            db_passwd = "hrs123456",
            db_name = "eZ7"
            )
        
        e = Employee()
        employee = e.get(ez.db_session, "C3001")
        print(employee.id, employee.name)
if __name__ == '__main__':
    unittest.main()
