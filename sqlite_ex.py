import sqlite3

conn=sqlite3.connect('webinfo.db')

c = conn.cursor()
            #text 문자 , real 정수,실수 둘다 포함
c.execute('''
create table if not exists stocks(
    no integer primary key,
    name text,      
    gender text,
    email text,
    year text
    )
''')
conn.commit()
conn.close()
# c.execute('''
# insert into stocks(date,trans,symbol,qty,price)
# values('2006-0105','BUY','aaa',100,35.14)
#  ''')

# symbol='aaa'
# c.execute("select * from stocks where symbol='%s'"%symbol)
# items=c.fetchall()

# for item in items:
#     print(item)


# t=('aaa',100)
# c.execute("select * from stocks where symbol=? and qty=?",t)
# print(c.fetchall())
# conn.close()