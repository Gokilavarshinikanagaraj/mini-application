=print("             AMAZON           ")
shopping_items=[{'id':1001,'name':'Oppo','available':45,'Price':20000,'Amount':21000},
              {'id':1002,'name':'Vivo','available':205,'Price':28000,'Amount':30000},
              {'id':1003,'name':'Redmi','available':35,'Price':25000,'AMmount':26000}]
shopping_items1=shopping_items
temp=[]
order=""
merchants=[{'id':2001,'name':'gokila','password':123},
           {'id':2002,'name':'varshini','password':456},
           {'id':2003,'name':'gokilavarshini','password':789}]
merchants1=merchants
temp1=[]
choose=""
def adminlogin():
    print("\n3=Add Merchant,4=Remove Merchant,5=Logout")
def userdisplay():
    for s in shopping_items:
        print(s['id'],s['name'],s['available'])
def addmerchants():
    n=int(input("\nEnter the merchant id to be added: "))
    for i in range(n):
        new_id=int(input("Enter id: "))
        new_name=input("Enter name: ")
        new_password=int(input("Enter the password: "))
        m=[{'id':new_id,'name':new_name,'password':new_password}]
        merchants.extend(m)
        print(merchants)
        adminlogin()
def removemerchant():
    print(merchants)
    n=int(input("\nEnter the merchant id to be added: "))
    for i in range(n):
        old_id=int(input("Enter id: "))
        old_name=input("Enter name: ")
        old_password=int(input("Enter the password: "))
        o=[{'id':old_id,'name':old_name,'password':old_password}]
        merchants.remove[o]
        print(merchants)
        adminlogin()
def logout():
    login()
def adminchoice():
    choice=int(input("Please enter choice: "))
    if (choice==3):
        addmerchants()
        adminlogin()
        adminchoice()
    elif(choice==4):
        removemerchant()
        adminlogin()
        adminchoice()
    elif(choice==5):
        logout()
        adminlogin()
        login()
    else:
        print("\nINVALID CHOICE")
        adminlogin()
        adminchoice()
def userlogin():
    print("\n6=Place order,7=Cancel order,8=Logout")
def placeorder():
    userdisplay()
    order_number=1
    print(shopping_items)
    p_id=int(input("\nEnter the id: "))
    for s in shopping_items:
        if s['id']==p_id:
            print(s['id'])
            order='s["id"]}\t{s["name"]}\t{s["available"]}\t\t{d["price"]}'
            confirm=input("\nDo you want to place an order above product: y/n ")
            if confirm=='y':
                print("\nSuccessfully placed the orderv:{} {}".format(s["id"],s["name"]))
                order_number+=1
                print("\nYour order number is: ",order_number)
                break
            elif confirm=='n':
                print("\nThe order is not placed.")
            else:
                print("\nINVALID CHOICE")
        else:
            print("\nINVALID CHOICE")
def cancelorder():
    found=True
    temp1=[]
    order_id=input("\nEnter the order_id: ")
    for s in shopping_items:
        found=s['id']==order_id
        if found==True:
            temp1.append(s)
        elif found==False:
            print("\nINVALID CHOICE")
    if len(temp1)==s:
         print("\nYOUR ORDERED IN IS PLACED")
    else:
        print(order_id, "is removed from the placed order")
def userchoice():
    choice=int(input("\nPlease enter choice: "))
    if (choice==6):
        placeorder()
        userlogin()
        userchoice()
    elif (choice==7):
        cancelorder()
        userlogin()
        userchoice()
    elif (choice==8):
        logout()
        login()
        
def login():
    print("\n1=Admin,2=User")
    choice=int(input("\nEnter the choice: "))
    if choice==1:
        print("Admin")
        password=int(input("\nEnter the password: "))
        if (password==123):
            adminlogin()
            adminchoice()
        else:
            print("\nINVALID PASSWORD")
    elif choice==2:
        print("User")
        password=input("\nEnter the password: ")
        if password=="abc":
            userlogin()
            userchoice()
        else:
            print("\nINVALID PASSWORD")
login()
        
