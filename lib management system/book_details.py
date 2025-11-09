from author import auth
from book import book
while True:
    print("1.add book 2.disp book 3.upd book 4.del book 5.search book 6.add author 7.disp author 8.search author 9.exit")
    ch=input("Enter Your Choice:")
    if ch=="1":
        bid=int(input("Enter Book ID:"))
        btitle=input("Enter Book Title:")
        aid=int(input("Enter Auth_ID:"))
        pubyear=int(input("Enter Pub_Year(YYYY):"))
        publisher=input("Enter Auth_Name:")
        totalcpy=int(input("Enter Total Copy:"))
        avlbcpy=int(input("Enter Availb Copy:"))
        obj=book(bid,btitle,aid,pubyear,publisher,totalcpy,avlbcpy)
        obj.add_book()
    elif ch=="2":
        obj=book()
        obj.disp_book()
    elif ch=="3":
        bid=int(input("Enter Upd Book ID:"))
        btitle=input("Enter Upd Book Title:")
        pubyear=int(input("Enter Upd Pub_Year(YYYY):"))
        totalcpy=int(input("Enter Total Copy:"))
        avlbcpy=int(input("Enter Availb Copy:"))
        obj=book(bid,btitle,pubyear=pubyear,totalcpy=totalcpy,avlbcpy=avlbcpy)
        obj.upd_book()
    elif ch=="4":
        bid=int(input("Enter del BookID:"))
        obj=book(bid)
        obj.del_book()
    elif ch=="5":
        bid=int(input("Enter Search BookID:"))
        obj=book(bid)
        obj.search_book()
    elif ch=="6":
        aid=int(input("Enter Auth_ID:"))
        aname=input("Enter Auth Name:")
        acountry=input("Enter Auth Country:")
        bk_writ=input("Enter Book Writ:")
        obj=auth(aid,aname,acountry,bk_writ)
        obj.add_auth()
    elif ch=="7":
        obj=auth()
        obj.disp_auth()
    elif ch=="8":
        aid=int(input("Enter Auth_ID:"))
        obj=auth(aid)
        obj.search_auth()
    elif ch=="8":
        print("Thank You.")
        break
    else:
        print("Invalid Choice")
        break