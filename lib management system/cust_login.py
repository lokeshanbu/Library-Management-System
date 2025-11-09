from customer import cust
from book import book
while True:
    print("1.add user 2.disp user 3.update user 4.delete user 5.search user 6.display book details 7.search book details 8.exit")
    ch=input("Enter your Choice:")
    if ch=="1":
        cid=int(input("Enter CustId:"))
        cname=input("Enter CustName:")
        cmail=input("Enter CustMail:")
        cphone=int(input("Enter CustPhone:"))
        cplace=input("Enter CustPlace:")
        obj=cust(cid,cname,cmail,cphone,cplace)
        obj.add_user()
    elif ch=="2":
        obj=cust()
        obj.disp_user()
    elif ch=="3":
        cid=int(input("Enter Cust_id:"))
        cname=input("Enter Upd Name:")
        cmail=input("Enter Upd Email:")
        cphone=int(input("Enter Upd Phone no:"))
        cplace=input("Enter Upd Place:")
        obj=cust(cid,cname,cmail,cphone,cplace)
        obj.upd_user()
    elif ch=="4":
        cid=int(input("Enter cust_id:"))
        obj=cust(cid)
        obj.del_user()
    elif ch=="5":
        cid=int(input("Enter Customer ID:"))
        obj=cust(cid)
        obj.search_user()
    elif ch=="6":
        obj=book()
        obj.disp_book()
    elif ch=="7":
        bid=int(input("Enter Search Book ID:"))
        obj=book(bid)
        obj.search_book()
    elif ch=="8":
        print("Thank You!")
        break
    else:
        print("Invalid Choice.")
        break
