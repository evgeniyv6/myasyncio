#!/usr/bin/env python

import io
from io import StringIO

orastr = '''
LIRL =
  (DESCRIPTION_LIST =
    (DESCRIPTION =
      (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1))
      (ADDRESS = (PROTOCOL = TCP)(HOST = myserver.example.com)(PORT = 1521))
    )
  )

SID_LIST_LIRL =
  (SID_LIST =
    (SID_DESC =
      (GLOBAL_DBNAME = orcl.example.com)
      (ORACLE_HOME = /u01/app/oracle/product/11.2.0.4/db_1)
      (SID_NAME = rl)
    )
  )
'''

mystrio = StringIO(orastr)

print(mystrio.readlines())
