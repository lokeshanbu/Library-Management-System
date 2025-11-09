from employee import emp
while True:
    print("1.sign-up employee 2.login employee 3.exit")
    ch=input("Enter your Choice:")
    if ch=="1":
        empid=int(input("Enter Emp_Id:"))
        empname=input("Enter Emp Name:")
        eemail=input("Enter Emp E-mail:")
        password=input("Enter Emp Password:")
        obj=emp(empid,empname,eemail,password)
        obj.signup_emp()
    elif ch=="2":
        eemail=input("Enter Emp E-mail:")
        password=input("Enter Emp Password:")
        obj=emp(eemail=eemail,password=password)
        obj.login_emp()
    elif ch=="3":
        print("Thank You!")
        break
    else:
        print("Enter a valid choice:")