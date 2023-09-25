# import mysql.connector
#
# con = mysql.connector.connect(host='localhost',
#                         user='root',
#                         password='Jovan@2023',
#                         database="mydb")
# curs = con.cursor()
# curs.execute("SELECT * FROM mydb.student")
#
# for val in curs:
#     print(val)
#
# con.close()

######################################################################33
# ('Ram', 'CSE', 85, 'B', 19)
# ('Nikhil', 'CSE', 98, 'A', 18)
# ('Nisha', 'CSE', 99, 'A', 18)
# ('Rohan', 'MAE', 43, 'B', 20)
# ('Amit', 'ECE', 24, 'A', 21)
# ('Anil', 'MAE', 45, 'B', 20)
# ('Megha', 'ECE', 55, 'A', 22)
# ('Sita', 'CSE', 95, 'A', 19)
############################################################################
import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',
                            user='root',
                            password='Jovan@2023',
                            database="mydb123")
    curs = con.cursor()
    # curs.execute("insert into mydb.student values('Ramya','ECE','46','B','18')")
    # con.commit()

    # curs.execute("SELECT * FROM mydb.student")
    # for val in curs:
    #     print(val)

    # curs.execute("update mydb.student set BRANCH='MEC' where BRANCH='MAE'")
    # con.commit()
    #
    # curs.execute("SELECT * FROM mydb.student")
    # for val in curs:
    #     print(val)

    curs.execute("delete from mydb.student where NAME='Ramya'")
    con.commit()
    curs.execute("SELECT * FROM mydb.student")
    for val in curs:
        print(val)
    con.close()
except:
    print("unsuccessful connection........")