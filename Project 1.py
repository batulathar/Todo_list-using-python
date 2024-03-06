from datetime import datetime as time1
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user=input("Enter your mysql user ID: "),
  password=input("Enter your mysql password: ")
)
mycursor=mydb.cursor()
y=True
while y==True:
    print("\t\t\t\t\t\t\t\tMenu \n1. Setup \n2. GO to todo application")
    mn=int(input("Enter your choice: "))
    if mn==1:
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()
        for database in databases:
            if 'todo_list' in database:
                print("Required database already exist.")
                rq=False
                break
            else:
                rq=True
                continue
        if rq==True:
            mycursor.execute("CREATE DATABASE todo_list;")
        mycursor.execute("USE todo_list;")
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        for table in tables:
            if 'todo' in table:
                print("Required table already exist.")
                rq1=False
                break
            else:
                rq1=True
                continue
        if rq1==True:
            mycursor.execute("CREATE TABLE todo (Title varchar(100), Created_Time time(0), Sub_Title varchar(100), Priority varchar(20), Status varchar(20));")
    elif mn==2:
        mycursor.execute("USE todo_list;")
        print("\n\n\n\t\t\t\t Main Menu \n1. Add \n2. Show \n3. Update \n4. Delete \n5. Search \n6. Exit")
        a=int(input("Enter the task number [1,2,3,4,5,6]: "))
        if a==1:
            title=input("Enter your Title: ")
            time=time1.now().strftime('%H:%M:%S')
            subtitle=input("Enter your  Sub Title: ")
            priority=input("Enter Priority ['High','Medium','Low']: ")
            status=input("Enter Status ['Completed','Pending']: ")
            if priority in ["High","Medium","Low"] and status in ["Completed","Pending"]:
                sql="INSERT INTO todo(Title, Created_Time, Sub_Title, Priority, Status) VALUES (%s, %s, %s, %s, %s)"
                val=(title, time, subtitle, priority, status)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
            else:
                print("Error!!! Incorrect priority or status entered")
                continue
        elif a==2:
            print("\n\nSelect Filter \n1. None \n2. Priority \n3. Status")
            a1=int(input("Enter Filter [1,2,3]: "))
            if a1==1:
                mycursor.execute("SELECT * FROM todo;")
                myresult = mycursor.fetchall()
                for x in myresult:
                    for i in range (0,len(x)):
                        if i!=1:
                            print(x[i],end=",\t")
                        elif i==1:
                            time_delta = x[i]
                            hours = time_delta.seconds // 3600
                            minutes = (time_delta.seconds % 3600) // 60
                            seconds = time_delta.seconds % 60
                            formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                            print(formatted_time,end=",\t")
                    print()
            elif a1==2:
                query1="SELECT * FROM todo WHERE Priority=%s;"
                cons=(input("Enter your priority ['High','Medium','Low']: "),)
                if cons in ['High','Medium','Low']:
                    mycursor.execute(query1,cons)
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        for i in range (0,len(x)):
                            if i!=1:
                                print(x[i],end=",\t")
                            elif i==1:
                                time_delta = x[i]
                                hours = time_delta.seconds // 3600
                                minutes = (time_delta.seconds % 3600) // 60
                                seconds = time_delta.seconds % 60
                                formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                                print(formatted_time,end=",\t")
                        print()
                else:
                    print("Invalid Input.")
            elif a1==3:
                query1="SELECT * FROM todo WHERE Status=%s;"
                cons=(input("Enter your Status ['Completed','Pending']: "),)
                if cons in ['Completed','Pending']:
                    mycursor.execute(query1,cons)
                    myresult = mycursor.fetchall()
                    if mycursor.countrow!=0:
                        for x in myresult:
                            for i in range (0,len(x)):
                                if i!=1:
                                    print(x[i],end=",\t")
                                elif i==1:
                                    time_delta = x[i]
                                    hours = time_delta.seconds // 3600
                                    minutes = (time_delta.seconds % 3600) // 60
                                    seconds = time_delta.seconds % 60
                                    formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                                    print(formatted_time,end=",\t")
                            print()
                    else:
                        print("Your Table is empty")
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
                continue
        elif a==3:
            old_title=input("Enter your Title: ")
            title=input("Enter your Updated Title: ")
            time=time1.now().strftime('%H:%M:%S')
            subtitle=input("Enter your Updated Sub Title: ")
            priority=input("Enter Updated Priority ['High','Medium','Low']: ")
            status=input("Enter Updated Status ['Completed','Pending']: ")
            if priority in ["High","Medium","Low"] and status in ["Completed","Pending"]:
                sql = "UPDATE todo SET Title=%s, Created_Time = %s,Sub_Title = %s, Priority = %s , Status = %s WHERE Title = %s"
                val=(title, time, subtitle, priority, status,old_title)
                mycursor.execute(sql, val)
                mydb.commit()
                if mycursor.rowcount!=0:
                    print(mycursor.rowcount, "record updated.")
                else:
                    print("Error 404! Title not found")
            else:
                print("Error!!! Incorrect priority or status entered")
                continue
        elif a==4:
            sql = "DELETE FROM todo WHERE Title = %s"
            cons = (input("Enter your Title: "),)
            mycursor.execute(sql,cons)
            mydb.commit()
            if mycursor.rowcount!=0:
                print(mycursor.rowcount, "record(s) deleted")
            else:
                print("Error 404! Title not found")
        elif a==5:
            sql = "SELECT * FROM todo WHERE Title = %s"
            cons = (input("Enter your Title: "),)
            mycursor.execute(sql,cons)
            myresult = mycursor.fetchall()
            if len(myresult)!=0:
                for x in myresult:
                    for i in range (0,len(x)):
                        if i!=1:
                            print(x[i],end=",\t")
                        elif i==1:
                            time_delta = x[i]
                            hours = time_delta.seconds // 3600
                            minutes = (time_delta.seconds % 3600) // 60
                            seconds = time_delta.seconds % 60
                            formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
                            print(formatted_time,end=",\t")
                    print()
            else:
                print("Error 404! Title not found")
        elif a==6:
            break
        else:
            continue
    else:
        continue
