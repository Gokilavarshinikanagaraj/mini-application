print("WELCOME TO ATM")
balance=100000
transation=5
amount={100:0,200:0,500:0,2000:0}
while True:
    print("\n1=ADMIN LOGIN,2=USER LOGIN,3=EXIT")
    person=int(input("\nENTER THE CHOISE: "))
    if(person==1):
        print("1=ADMIN")
        while True:
            print("\n4=LOAD,5=SHOW,6=EXIT")
            person=int(input("\nENTER THE CHOISE: "))
            if(person==4):
                print("4=LOAD")
                for i in amount.keys():
                    n=int(input("\nENTER NO.OF "+str(i)+ " Notes: "))
                    amount[i]+=n
                print("AMOUNT ADDED SUCCESSFULLY")
                #break
            elif(person==5):
                for j in amount:
                    print (j,amount[j]) 
            else:
                print("EXIT")
            break
    elif(person==2):
        print("2=USER LOGIN")
        print("INSERT ATM CARD")
        while True:
            pin=int(input("\nPLEASE ENTER YOUR FOUR DIGIT PIN: "))
            if (pin==1006):
                print("YOU ENTERED YOUR PIN CORRECTLY")
                while True:
                    print("\n6=VIEW BALANCE,7=WITHDRAW,8=DEPOSIT,9=TRANSACTION,10=PIN CHANGE,11=EXIT")
                    person=int(input("\nENTER THE CHOICE"))
                    if(person==6):
                        print(balance)
                    elif(person==7):
                        withdraw=int(input("\nENTER THE WITHDRAW AMOUNT"))
                        print('\nWITHDRW AMOUNT')
                        if (balance>=withdraw):
                            print("\nCOLLECT YOUR CASH")
                            balance=balance-withdraw
                            print(balance)
                        else:
                            print("INVALID AMOUNT")
                            #break
                    elif(person==8):
                        deposit=float(input("\nENTER THE DEPOSIT AMOUNT"))
                        print(deposit)
                        balance=balance+deposit
                        print(balance)
                    elif(person==9):
                        transaction=float(input("\nENTER THE TRANSACTION AMOUNT"))
                        print("\nTRANSACTION SUCCESSFULLY")
                        balance=balance-transaction
                        print(balance)
                    elif(person==10):
                        print("CHANGE PIN NUMBER")
                        new_pin=int(input("\nENTER NEW PIN"))
                        if (new_pin==1008):
                            print("\nPIN NUMBER CHANGED SUCCESSFULLY")
                        else:
                            print("ENTER NUMBER SAME AS OLD PIN NUMBER")
                    elif(person==11):
                        print("EXIT")
                        break
                    else:
                        print("INVALID CHOICE")
                    break
            else:
                break
    elif(person==3):
        print("EXIT")
    else:
        break
    
        
                
        
 

            
                









                        
