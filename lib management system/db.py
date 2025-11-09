import mysql.connector
def data():
    db=mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='libry'
    )
    return db
