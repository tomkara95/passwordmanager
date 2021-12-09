import mysql.connector

mydb = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='passwords')

mycursor = mydb.cursor()


exitflag=False
while exitflag==False:
    choiceflag=True
    print("MENU")
    print("1.New Entry")
    print("2.Call Entry")
    print("3.Modify Entry")
    choice = int (input("Select 1 2 or 3: "))
    while choiceflag==True:
        if choice<=3 and choice>=1:
            choiceflag=False 
        else:
            print("Not accepted choice, ")
            choice = int (input(" please select 1 2 or 3: "))


    if choice == 1:
        print('give a new account: ')
        x = input("webpage: ")
        y = input("username: ")
        newsql = "SELECT * FROM accounts WHERE webpage = %s and username = %s"
        newval = (x,y, )
        mycursor.execute(newsql, newval)
        myresult = mycursor.fetchall()
        if myresult:
            print('already exists')
        else:
            z = input("pass: ")
            sql = "INSERT INTO accounts (webpage, username, pass) VALUES (%s, %s, %s)"
            val = (x, y, z)
            mycursor.execute(sql, val)
            mydb.commit()      
            print ("New entry made successfully! ")
            

    if choice == 2:
        flag= True
        while flag== True:
            user_input = input ("Account you are looking for: ")
            sql1 = "SELECT * FROM accounts WHERE webpage = %s "
            old1 = (user_input,)
            mycursor.execute(sql1,old1)
            myresult = mycursor.fetchall()
            if not myresult:
                print ('It does not exist ')
            else:
                for i in myresult:
                    print(i)
                flag = False
        

    if choice ==3:
        print('give an existing account: ')
        x = input("webpage: ")
        y = input("username: ")
        oldsql = "SELECT * FROM accounts WHERE webpage = %s and username= %s"
        oldval = (x,y, )

        mycursor.execute(oldsql, oldval)

        myresult2 = mycursor.fetchall()

        if myresult2:
            z = input("newpass: ")
            sqlnew = "UPDATE accounts SET pass = %s WHERE webpage = %s and username= %s "
            valnew = (z,x,y)
            mycursor.execute(sqlnew, valnew)
            mydb.commit()
            print("password changed! ")
            
        else:
            print('Account does not exist! ')
    exittemp= True
    while exittemp==True:
        exit = input("exit? y/n _")
        if exit == "y" or exit=="Y":
            exittemp=False
            exitflag=True
        elif exit == "n" or exit == "N":
            exittemp=False
            choiceflag=True
        else:
            print("not accepted answer,try again : ")
    
                
                



