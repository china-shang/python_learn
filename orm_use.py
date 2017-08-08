# !/usr/bin/env python
# coding = utf-8

from sqlalchemy import create_engine
import sqlalchemy

sqlalchemy.column
engine = create_engine("mysql://root@127.0.0.1:3306/base1", max_overflow=5)
cur = engine.execute('select * from students')
# fjdif
