
user={"abc":"1","bcd":"2","cde":"3","def":"4"}
user_info={"a":("1","chennai to salem","500"),
           "b": ("2","chennai to tirupur","500"),
           "c":("3","chennai to erode","500"),
           "d":("4","chennai to salem","500")}
station={"coimbatore":1,"tirupur":3,"Erode":3,"salem":4}
chennai={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'empty'}
tirupur={1: "a", 2: "empty", 3: "c", 4: "empty", 5: "empty"}
erode={1: "a", 2: "empty", 3: "c", 4: "empty", 5: "empty"}
salem={1: "a", 2: "empty", 3: "c", 4: "empty", 5: "empty"}
seat_info={1:chennai,2:tirupur,3:erode,4:salem}
def userfun():
        global station
        global user
        global coimbatore
        global user_name
        global seat_info
        global coimbatore
        global tirupur
        global erode
        global salem
        global user_info
        station_lst=list(station)
        print("1.Ticket booking\n2.Ticket info\n3.Ticket Cancellation")
        choice=int(input("Enter the choice:"))
        if(choice==1):
            boarding=str(input("From:"))
            station1=str(input("To:"))
            a=station.get(boarding)
            dc={"chennai":chennai,"tirupur":tirupur,"erode":erode,"salme":salem}
            dc1={"chennai":1,"tirupur":2,"erode":3,"salem":4}
            if(int(a)>=1):
               seat_pro=[]
               seat_lst = []
               print("Ticket cost:", 500)
               for i in range(1,6):
                   for pro in range(dc1[boarding],dc1[station1]+1):
                       if(seat_info[pro].get(i)== "empty"):
                               seat_pro.append(i)
                               if(((dc1.get(station1)-dc1.get(boarding))+1)==seat_pro.count(i)):
                                    seat_lst.append(i)
               if(len(seat_lst)==1):
                           print("available seat No:")
                           print("only seat no:",seat_lst[0],"is availbale")
                           choice1 = str(input("Are u sure u want to book the seat:Y/n:"))
                           if (choice1 == "y"):
                               for j in range(len(seat_lst)):
                                   dic1={"coimbatore":1,"tirupur":2,"erode":3}
                                   dic={"tirupur":3,"erode":4,"saleml":5}
                                   for y in range(dic1.get(boarding),dic.get(station1)):
                                        seat_info[y].update({seat_lst[0]: user_name})
                               station_keys=list(station.keys())
                               count=0
                               for z in range(len(station_keys)):
                                   if(station.get(z)=="empty"):
                                       count+=1
                                       station.update({z:count})
                               user_info.update({user_name: ("          ", str(seat_lst[0]), "       ", boarding, "to", station1, "      ", "500")})
                               available_seat = station.get(boarding) - 1
                               station.update({boarding: available_seat})
                               print("*Ur seat is booked,have a happy journey*")
               elif(len(seat_lst)>1):
                           print("available seat No:")
                           print(seat_lst)
                           choice=int(input("select one of the seat no mentioned above:"))
                           if(choice in seat_lst):
                              choice1 = str(input("Are u sure u want to book the seat:Y/n:"))
                              if (choice1 == "y"):
                                   for j in range(len(seat_lst)):
                                       dic1 = {"chennai": 1, "tiruppur": 2, "erode": 3}
                                       dic = {"tirupur": 3, "erode": 4, "salem": 5}
                                       for y in range(dic1.get(boarding), dic.get(station1)):
                                           seat_info[y].update({choice: user_name})
                                   station_keys = list(station.keys())
                                   count = 0
                                   for z in range(len(station_keys)):
                                     if (station.get(z) == "empty"):
                                           count += 1
                                           station.update({z: count})
                                   dc[boarding].update({choice: user_name})
                                   dc[station1].update({choice: user_name})
                                   available_seat = station.get(boarding) - 1
                                   station.update({boarding: available_seat})
                                   user_info.update({user_name: ("          ",str(choice),"       ",boarding,"to",station1,"      ","500")})
                                   print("*Ur seat is booked,have a happy journey*")
               else:
                   print("No seats is available for salem,U may choose in between station")
            else:
                print("No seats is available")
        elif(choice==2):
            if(user_name not in user.keys()):
                print("No booking yet")
            else:
                print("Name       seat no        Board to Deboard:         ticket cost")
                print(user_name, *user_info.get(user_name))
        else:
            confirm=str(input("do you want to cancel the booking y/n:"))
            if(confirm=="y"):
                print("For Confirmation")
                choice1=str(input("enter the name"))
                choice=int(input("enter the seat number:"))
                user.pop(user_name)
                user_info.pop(user_name)
                for i in range(1,5):
                    seat_info[i].update({choice:"empty"})
                print("cancellation is done")
                intro()
            else:
                intro()
def intro():
    global station
    global user_name
    global chennai
    global tirupur
    global erode
    global dindigul
    print("1.user\n2.exit")
    choice=int(input("Enter the choice:"))
    if(choice==1):
        while True:
            print("1.new user\n2.existing user\n3.exit")
            choice=int(input("Enter the choice:"))
            if(choice==1):
                user_name=str(input("Enter the name:"))
                user_password=str(input("Enter the password:"))
                userfun()
                user.update({user_name: user_password})
                intro()
            elif(choice==2):
                user_name=str(input("Enter the name:"))
                user_password=str(input("Enter the password:"))
                if((user_name,user_password) in user.items()):
                    userfun()
                else:
                    print("Invalid username or password")
            else:
                intro()
    else:
            intro()
intro()
