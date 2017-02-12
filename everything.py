#! /usr/bin/env python
# Written by Joshua Jordi

import sqlite3



sqlite_file = './db.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table_1 = 'fileName'
table_2 = 'fileLoc'

new_field = 'temp'
field_type = 'char'

#c.execute("create table {tn} ({nf} {ft})"\
#          .format(tn=table_1, nf=new_field, ft=field_type))

#c.execute('create table {tn} ({nf} {ft})'\
#          .format(tn=table_2, nf=new_field, ft=field_type))

c.execute('select * from fileName')

conn.commit()
conn.close()

