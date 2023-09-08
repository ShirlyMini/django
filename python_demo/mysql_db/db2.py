import mysql.connector

# con = mysql.connector.connect(host='localhost', # '127.0.0.1'
#                         user='root',
#                         password='Jovan@2023',
#                         )
#
# cur = con.cursor()
# cur.execute("CREATE DATABASE mydb2")
#
# con.close()
#con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')
#print(con.version)

# https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html


con = mysql.connector.connect(host='localhost', # '127.0.0.1'
                        user='root',
                        password='Jovan@2023',
                        database='mydb2')
cur = con.cursor()
#var = "CREATE TABLE student(id int, name varchar(20), dept varchar(10))"
#cur.execute("CREATE TABLE student(id int, name varchar(20), dept varchar(10))")
#data = "insert into student (id, name,dept) values (101, 'kiran', 'cse')"
#val = ("101", "kiran", "cse")
#cur.execute(data)

data = "insert into student (id, name,dept) values (%s, %s, %s)"
val = [("102", "stud1", "cse"),
       ("103", "stud2", "bcom"),
       ("104", "stud3", "math"),
       ("105", "stud4", "cse"),
       ("106", "stud5", "science"),
       ("107", "stud6", "cse")]
#cur.executemany(data, val)
cur.execute("update student set dept='biology' where id=105")

cur.execute("select * from student where id=105")
for val in cur:
    print(val)
con.commit()
con.close()
