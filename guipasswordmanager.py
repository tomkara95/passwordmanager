from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

mydb = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='passwords')

mycursor = mydb.cursor()


mydb.commit()



#mydb.close()

root = Tk()
root.title("Password Manager")
title_label = Label(root,text="Password Manager",font=("Arial",16))
title_label.grid(row=0,column=2,columnspan=4,pady=10)



def Apply():
    sql = "INSERT INTO accounts (webpage, username, pass) VALUES (%s, %s, %s)"
    val = (str(new_web.get()), str(new_user.get()),str(new_pass.get()))
    mycursor.execute( sql, val)
    mydb.commit()      
    clear_all_entry()


def call_apply():
    user_name= Tk()
    user_name.title("username and password")
    newsql = "SELECT * FROM accounts WHERE webpage = %s "
    newval = (str(new_e1.get()) ,)
    mycursor.execute(newsql, newval)
    myresult = mycursor.fetchall()
    '''for x in myresult:
        
            search_label = Label (user_name,text=x )
            search_label.pack()
        except:
            errorlabel = Label (user_name,text="does not exists") 
            errorlabel.pack()   
    clear_all_call()
'''

def clear_all_entry():
    top = Toplevel()
    new_web.delete(0,END)
    new_user.delete(0,END)
    new_pass.delete(0,END)
    global mylabel
    mylabel = Label (top,text="Entry made successfully")
    mylabel.grid(row=6,column=1)
    

def clear_all_call():
    new_e1.delete(0,END)
    #new_user1.delete(0,END)
    #new_pass1.delete(0,END)
    
    

def clear_all_modify():
    new_e2.delete(0,END)
    new_user2.delete(0,END)
    new_pass2.delete(0,END)    
    

def open_new_entry():
    global new_web
    global new_user
    global new_pass
    top = Toplevel()
    top.title("New entry")
    top.geometry('400x400')
    top.resizable(False,False)
    title_entry = Label(top,text="New Entry",font=("Arial",16))
    title_entry.grid(row=0,column=1,columnspan=3,pady=10)
    new_web_label= Label (top,text="New website").grid(row=1,column=0)
    new_web = Entry(top , width = 30 )
    new_web.grid(row=1,column=1)
    new_user_label= Label (top,text="New username").grid(row=2,column=0)
    new_user = Entry(top , width = 30)
    new_user.grid(row = 2, column=1)
    new_pass_label= Label (top,text="New password").grid(row=3,column=0)
    new_pass = Entry(top , width = 30)
    new_pass.grid(row = 3, column=1)
    button_quit_entry = Button(top, text="Back",padx=15,pady=10,command=top.destroy)
    button_quit_entry.grid(row=4,column=1,columnspan= 1)
    button_clear_entry= Button(top,text="Clear",padx=15,pady=10,command=clear_all_entry)
    button_clear_entry.grid(row=4,column=2,columnspan= 1)
    button_apply = Button(top , text="Apply",padx=15,pady=10,command=Apply )
    button_apply.grid(row=4,column=3,columnspan= 1)
    

def open_call_entry():
    global new_e1
    top = Toplevel()
    top.title("Call entry")
    top.geometry('400x400')
    top.resizable(False,False)
    title_call = Label(top,text="Call an Entry",font=("Arial",16))
    title_call.grid(row=0,column=1,columnspan=3,pady=10)
    new_e1_label= Label (top,text="Website").grid(row=1,column=0)
    new_e1 = Entry(top , width = 30 )
    new_e1.grid(row=1,column=1)
    button_quit_call = Button(top, text="Back",padx=15,pady=10,command=top.destroy)
    button_quit_call.grid(row=4,column=1,columnspan= 1)
    button_clear_call= Button(top,text="Clear",padx=15,pady=10,command=clear_all_call)
    button_clear_call.grid(row=4,column=2,columnspan= 1)
    button_apply = Button(top , text="Apply",padx=15,pady=10,command=call_apply )
    button_apply.grid(row=4,column=3,columnspan= 1)

def open_modify_entry():
    global new_e2
    global new_user2
    global new_pass2
    top = Toplevel()
    top.title("Modify entry")
    top.geometry('400x400')
    top.resizable(False,False)
    title_modify = Label(top,text="Modify an Entry",font=("Arial",16))
    title_modify.grid(row=0,column=1,columnspan=3,pady=10)
    new_e2_label= Label (top,text="Website").grid(row=1,column=0)
    new_e2 = Entry(top , width = 30 )
    new_e2.grid(row=1,column=1)
    new_user2_label= Label (top,text="Username").grid(row=2,column=0)
    new_user2 = Entry(top , width = 30)
    new_user2.grid(row = 2, column=1)
    new_pass2_label= Label (top,text="New password").grid(row=3,column=0)
    new_pass2 = Entry(top , width = 30)
    new_pass2.grid(row = 3, column=1)
    button_quit_modify = Button(top, text="Back",padx=15,pady=10,command=top.destroy)
    button_quit_modify.grid(row=4,column=1,columnspan= 1)
    button_clear_modify= Button(top,text="Clear",padx=15,pady=10,command=clear_all_modify)
    button_clear_modify.grid(row=4,column=2,columnspan= 1)
    button_apply = Button(top , text="Apply",padx=15,pady=10,command=Apply )
    button_apply.grid(row=4,column=3,columnspan= 1)



root.geometry('500x500')
root.resizable(False,False)

button_1 = Button(root, text ="New Entry",command=open_new_entry)
button_2 = Button(root, text ="Call Old Entry",command=open_call_entry)
button_3 = Button(root, text ="Modify Old Entry",command=open_modify_entry)
button_quit = Button(root, text="Exit",padx=15,pady=10,command=root.quit)


button_1.grid(row=1,column=1,columnspan= 1,padx=30,pady=20)
button_2.grid(row=2,column=1,columnspan= 1,padx=30,pady=20)
button_3.grid(row=3,column=1,columnspan= 1,padx=30,pady=20)
button_quit.grid(row=4,column=1,columnspan= 1)

mycursor.execute("SELECT * FROM accounts")
result = mycursor.fetchall()
for x in result:
    print(x)


mainloop()
