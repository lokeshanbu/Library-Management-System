import os
while True:
    print("1.Customer Login 2.Employee Login 3.Exit")
    ch=input("Enter Your Choice:")
    if ch=="1":
        os.system("python cust_login.py")
    elif ch=="2":
        os.system("python emp_login.py")
    elif ch=="3":
        print("Thank You!")
        break
    else:
        print("Enter a valid choice.")