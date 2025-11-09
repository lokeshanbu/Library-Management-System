from db import data
from book import book
class cust:
    def __init__(s,cid=0,cname="",cmail="",cphone=0,cplace=""):
        s.cid=cid
        s.cname=cname
        s.cmail=cmail
        s.cphone=cphone
        s.cplace=cplace
    def add_user(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("INSERT INTO customer(cust_id,cname,cmail,cphone,cplace,cjoined) VALUES(%s,%s,%s,%s,%s)",
                       (s.cid, s.cname, s.cmail, s.cphone, s.cplace))
        db.commit()
        print("User Added Successfully!")
        cursor.close()
        db.close()
    def disp_user(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM customer")
        res=cursor.fetchall()
        for ele in res:
            print(ele)
        cursor.close()
        db.close()
    def upd_user(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("UPDATE customer SET cname=%s, cmail=%s, cphone=%s, cplace=%s WHERE cust_id=%s",
                       (s.cname,s.cmail,s.cphone,s.cplace,s.cid))
        db.commit()
        print("User Updated Successfully.")
        cursor.close()
        db.close()
    def del_user(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("DELETE FROM customer WHERE cust_id=%s",(s.cid,))
        db.commit()
        print("User removed successfully.")
        cursor.close()
        db.close()
    def search_user(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM customer WHERE cust_id=%s",(s.cid,))
        res=cursor.fetchall()
        if res:
            print("Yes, User Found!")
            print(res)
        else:
            print("User Not Found.")
        db.commit()
        cursor.close()
        db.close()
    def disp_book(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT bk_id,btitle,pub_year,total_copy,avlb_copy FROM book")
        res=cursor.fetchall()
        for i in res:
            print(i)
        print("Book Details Fetched Successfully.")
        cursor.close()
        db.close()
    def search_book(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("SELECT * FROM book WHERE bk_id=%s",(s.bid,))
        res=cursor.fetchall()
        if res:
            print("Book Found!")
            for ele in res:
                print(ele)
        else:
            print("Book Not Found.")
        cursor.close()
        db.close()
        