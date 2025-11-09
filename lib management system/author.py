from db import data
class auth:
    def __init__(s,aid=0,aname="",acountry="",bk_writ=""):
        s.aid=aid
        s.aname=aname
        s.acountry=acountry
        s.bk_writ=bk_writ
    def add_auth(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("INSERT INTO author(aut_id,aname,acountry,bk_writ) VALUES (%s,%s,%s,%s)",
                       (s.aid,s.aname,s.acountry,s.bk_writ))
        db.commit()
        print("Author Details Added Successful!")
        cursor.close()
        db.close()
    def disp_auth(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM author")
        res=cursor.fetchall()
        for i in res:
            print(i)
        cursor.close()
        db.close()
    def search_auth(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT aut_id,aname,acountry FROM author WHERE aut_id=%s",(s.aid,))
        res=cursor.fetchall()
        if res:
            print("Author Found.")
            print(res)
        else:
            print("Author Not Found.")
        db.commit()
        cursor.close()
        db.close()