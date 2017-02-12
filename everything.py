#! /usr/bin/env python
# Written by Joshua Jordi

import sqlite3
import os

if (os.path.isfile('db.sqlite')):
    os.remove('db.sqlite')

sqlite_file = './db.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table1 = 'file'

field0 = 'priKey'
field1 = 'filePath'
field2 = 'fileName'

keyType = 'INTEGER'
fieldType = 'TEXT'

c.execute('create table {tn} ({nf} {ft})'\
          .format(tn=table1, nf=field0, ft=keyType))

c.execute('alter table {tn} add column "{cn}" {ct}'\
          .format(tn=table1, cn=field1, ct=fieldType))

c.execute('alter table {tn} add column "{cn}" {ct}'\
          .format(tn=table1, cn=field2, ct=fieldType))


conn.commit()
conn.close()
