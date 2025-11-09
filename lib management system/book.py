from db import data
class book:
    def __init__(s,bid=0,btitle="",aid=0,pubyear=0,publisher="",totalcpy=1,avlbcpy=1):
        s.bid=bid
        s.btitle=btitle
        s.aid=aid
        s.pubyear=pubyear
        s.publisher=publisher
        s.totalcpy=totalcpy
        s.avlbcpy=avlbcpy
    def add_book(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("INSERT INTO book(bk_id,btitle,aut_id,pub_year,publisher,total_copy,avlb_copy) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (s.bid,s.btitle,s.aid,s.pubyear,s.publisher,s.totalcpy,s.avlbcpy))
        db.commit()
        print("Book is Added Successfully!")
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
    def upd_book(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("UPDATE book SET btitle=%s,pub_year=%s,total_copy=%s,avlb_copy=%s WHERE bk_id=%s",
                       (s.btitle,s.pubyear,s.totalcpy,s.avlbcpy,s.bid))
        db.commit()
        print("Book Updated Successfully.")
        cursor.close()
        db.close()
    def del_book(s):
        db=data()
        cursor=db.cursor()
        cursor.execute("DELETE FROM book WHERE bk_id=%s",(s.bid,))
        db.commit()
        print("Book Deleted Successfully.")
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
