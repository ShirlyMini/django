import mysql.connector

con = mysql.connector.connect(host='localhost', # '127.0.0.1'
                        user='root',
                        password='Jovan@2023',
                        database="mydb2")

cur = con.cursor()
cur.execute("SELECT * FROM student;")
for val in cur:
    print(val)

con.close()

# insert data1
# insert data2
# savepoint name

# update data2
# rollback to savepoint name


