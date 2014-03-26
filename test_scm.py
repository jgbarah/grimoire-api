# -*- coding: utf-8 -*-

## Copyright (C) 2014 Bitergia
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
## Unit tests for scm.py
## 
## Authors:
##   Jesus M. Gonzalez-Barahona <jgb@bitergia.com>
##

from datetime import datetime
from scm import SCM, PeriodCondition
import unittest

database = 'mysql://jgb:XXX@localhost/vizgrimoire_cvsanaly'
# Set UTF-8, and avoid the DBAPI Unicode support, to use SQLAlchemy's,
# which is said to be more efficient
database += '?charset=utf8&use_unicode=0'

# class TestBuildSession (unittest.TestCase):

#     def setUp (self):
#         self.database = database

#     def test_get_session (self):

#         session = buildSession(database=self.database, echo=False)

class TestSCM (unittest.TestCase):

    def setUp (self):

        self.database = database
        self.start = datetime(2013,11,13)
        self.end = datetime(2014,2,1)


    def test_no_condition (self):
        """Test SCM object with no conditions"""

        data = SCM (database = database, var = "ncommits")
        self.assertEqual (data.total(), 4465)

    def test_period_condition (self):
        """Test SCM object with a period condition"""

        period = PeriodCondition (start = self.start, end = None)
        data = SCM (database = database, var = "ncommits",
                    period = period)
        self.assertEqual (data.total(), 839)
        period = PeriodCondition (start = self.start, end = self.end)
        data = SCM (database = database, var = "ncommits",
                    period = period)
        self.assertEqual (data.total(), 730)



if __name__ == "__main__":
    unittest.main()