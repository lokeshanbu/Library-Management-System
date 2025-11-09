import os
from db import data
class emp:
    def __init__(s,empid=0,empname="",eemail="",password=""):
        s.empid=empid
        s.empname=empname
        s.eemail=eemail.strip()
        s.password=password.strip()
    def signup_emp(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("INSERT INTO emp(eid,ename,email,pswd) VALUES(%s,%s,%s,%s)",
                       (s.empid,s.empname,s.eemail,s.password))
        db.commit()
        print("Employee Sign-up Successfully!")
        cursor.close()
        db.close()
    def login_emp(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM emp WHERE email=%s AND pswd=%s",(s.eemail,s.password))
        res=cursor.fetchone()
        if(res):
            print(f'Welcome Mr/Ms.{res[1]}! Login successful.')
            os.system("python book_details.py")
        else:
            print("Invalid employee details, Please check once.")
        cursor.close()
        db.close()