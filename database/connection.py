import cx_Oracle

conStr  = 'rm95028/261203:1521/orcl'

conn = cx_Oracle.connect(conStr)
cur = conn.cursor()

conn =  None

try:
    conn = cx_Oracle.connect(conStr)
    cur = conn.cursor 

except Exception as err:
    print('Error while connectiong in the db')
    print(err)

finally:
    if (conn):
        cur.close()

conn.close()

